from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
import requests
import json
from .models import Transactions

MERCHANT = ''
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"
amount = 11000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = 'email@example.com'  # Optional
mobile = ''  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://localhost:8000/gateway/verify/'


def send_request(request):
    resp = {"error": "amount not set", "state": False, "authority": ""}


    amount = request.POST.get("amount", None)
    print(amount)
    if not amount:
        return JsonResponse(resp)
    try:
        amount = int(amount)
        amount_r = amount * 10
    except (ValueError, TypeError):
        return JsonResponse(resp)
    req_data = {
        "merchant_id": MERCHANT,
        "amount": amount_r,
        "callback_url": CallbackURL,
        "description": description,
        "metadata": {"mobile": mobile, "email": email}
    }
    req_header = {"accept": "applicajsontion/",
                  "content-type": "application/json'"}
    req = requests.post(url=ZP_API_REQUEST, data=json.dumps(
        req_data), headers=req_header)
    authority = req.json()['data']['authority']
    trans = Transactions()
    trans.user = request.user
    trans.authority = authority
    trans.amount = amount
    trans.save()

    if len(req.json()['errors']) == 0:
        resp["authority"] = authority
        resp["state"] = True
        resp["error"] = ""
        return JsonResponse(resp)
        # return redirect(ZP_API_STARTPAY.format(authority=authority))
    else:
        e_code = req.json()['errors']['code']
        e_message = req.json()['errors']['message']
        return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")



def verify(request):
    t_status = request.GET.get('Status')
    t_authority = request.GET['Authority']
    if t_status == 'OK':
        req_header = {"accept": "application/json",
                      "content-type": "application/json'"}
        try:
            trans = Transactions.objects.get(authority=t_authority)
        except Transactions.DoesNotExist:
            return HttpResponse('Transaction Not Found')
        req_data = {
            "merchant_id": MERCHANT,
            "amount": amount,
            "authority": t_authority
        }
        req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
        if len(req.json()['errors']) == 0:
            t_status = req.json()['data']['code']
            if t_status == 100:
                import datetime
                from cart.models import Cart
                from HirMethods.Tamam import num_sep
                from factor.models import Factors, FacotrProduct
                trans.state = 1
                trans.payment_date = datetime.datetime.now()
                trans.ref_id = req.json()['data']['ref_id']
                trans.save()
                c = Cart.objects.filter(id_user=trans.user)
                user_factor = Factors()
                user_factor.id_user = trans.user
                user_factor.payment_date = datetime.datetime.now()
                user_factor.state = 1
                user_factor.ref_id = req.json()['data']['ref_id']
                user_factor.creat_date = datetime.datetime.now()
                user_factor.save()
                user_factor = Factors.objects.get(ref_id=req.json()['data']['ref_id'], id_user=trans.user)
                pro_list = []
                gheymat = total_price = 0
                for i in c:
                    show_price = num_sep(i.unit_price)
                    show_total = num_sep(i.total_price)
                    pro_list.append([i.id_product.name, i.count, show_price, show_total, i.id_product.id,
                                     i.id_product.category.name])
                    total_price += i.total_price
                    prod_factors = FacotrProduct()
                    prod_factors.id_factor = user_factor
                    prod_factors.id_product = i.id_product
                    prod_factors.count = i.count
                    prod_factors.unit_price = i.unit_price
                    prod_factors.total_price = i.total_price
                    prod_factors.save()
                gheymat = total_price
                user_factor.total_price = gheymat
                user_factor.save()
                total_price = num_sep(total_price)
                context = {
                    "amount": trans.amount,
                    "pro": pro_list,
                    "total_price": total_price,
                    "show_sabad": gheymat,
                    "RefID": req.json()['data']['ref_id']
                }
                c.delete()
                return render(request, "cart/factor.html", context={"data": context})
            elif t_status == 101:
                from cart.models import Cart
                from HirMethods.Tamam import num_sep, re100
                from factor.models import Factors, FacotrProduct
                try:
                    c = Cart.objects.filter(id_user=trans.user)
                    user_factor = Factors.objects.get(ref_id=req.json()['data']['ref_id'], id_user=trans.user)
                    pro_list = []
                    gheymat = total_price = 0
                    for i in c:
                        show_price = num_sep(i.unit_price)
                        show_total = num_sep(i.total_price)
                        pro_list.append([i.id_product.name, i.count, show_price, show_total, i.id_product.id,
                                         i.id_product.category.name])
                        total_price += i.total_price
                    total_price = num_sep(total_price)
                    context = {
                        "amount": trans.amount,
                        "pro": pro_list,
                        "total_price": total_price,
                        "show_sabad": gheymat,
                        "RefID": req.json()['data']['ref_id']
                    }
                    c.delete()
                    return render(request, "cart/factor.html", context={"data": context})
                except Factors.DoesNotExist:
                    context = re100(req, t_authority)
                    return render(request, "cart/factor.html", context={"data": context})
            else:
                import datetime
                trans.state = 0
                trans.payment_date = datetime.datetime.now()
                # trans.ref_id = req.json()['data']['ref_id']
                trans.save()
                # return HttpResponse('Transaction failed.\nStatus: ' + str(
                #     req.json()['data']['message']
                # ))
                return redirect("cart_home")
        else:
            e_code = req.json()['errors']['code']
            e_message = req.json()['errors']['message']
            import datetime
            trans.state = 0
            trans.payment_date = datetime.datetime.now()
            # trans.ref_id = req.json()['data']['ref_id']
            trans.save()
            return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
    else:
        return HttpResponse('Transaction failed or canceled by user')
