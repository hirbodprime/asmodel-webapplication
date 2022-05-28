from django.http import HttpResponse, JsonResponse
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from HirMethods.methods import num_sep


@login_required(login_url="/account/login")
def CarTpageView(request):
    from .models import Cart
    user = request.user
    cart = Cart.objects.filter(id_user=user)
    pro_list = []
    total_price = 0
    for i in cart:
        show_price = num_sep(i.id_product.price)
        show_total = num_sep(i.total_price)
        pro_list.append([i.id_product.ProductName, i.id_product.image, i.count, show_price, show_total , i.id_product.id , i.id])
        total_price += i.total_price
        total_price1 = total_price

    total_price = num_sep(total_price)
    return render(request, "shop/cart.html", {"cart": pro_list, "total_price": total_price , 'show_sabad':total_price1})
    


@login_required(login_url="/account/login")
def get_mycart(req):
    """ get all of cart for user """
    pro_dict = {}
    if req.user and req.user.is_authenticated:
        from .models import Cart
        cart = Cart.objects.filter(id_user=req.user)
        if cart.count() > 0:
            for c in cart:
                pro_dict.update({c.id_product.id: [c.id_product.ProductName, c.count, c.total_price]})

        # print(pro_dict)
    return JsonResponse(pro_dict, json_dumps_params={'ensure_ascii': False}, safe=True)

@login_required(login_url="/account/login")
def add_api_cart(req):
    """ api for add product in cart of user """
    """
        models field :
            id_product 
            id_user
            count
            total_price
    """
    pro_dict = {}
    if req.method == "POST":
        id_pro = req.POST.get("id_pro", 0)
        user_id = req.POST.get("user_id", 0)
        try:
            id_pro = int(id_pro)
        except (ValueError, TypeError, SyntaxError):
            return JsonResponse(pro_dict, json_dumps_params={'ensure_ascii': False}, safe=True)
        if not id_pro or id_pro <= 0:
            return JsonResponse(pro_dict, json_dumps_params={'ensure_ascii': False}, safe=True)
        if user_id:
            from django.contrib.auth.models import User
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                print("User.DoesNotExist")
                return JsonResponse(pro_dict, json_dumps_params={'ensure_ascii': False}, safe=True)
        else:
            print("user_id bug")
            return JsonResponse(pro_dict, json_dumps_params={'ensure_ascii': False}, safe=True)
        from shop.models import productmodel
        from .models import Cart
        try:
            p = productmodel.objects.get(deleted=False, id=id_pro)
        except productmodel.DoesNotExist:
            return JsonResponse(pro_dict, json_dumps_params={'ensure_ascii': False}, safe=True)
        try:
            cart = Cart.objects.get(id_user=user, id_product=p)
            c_count = cart.count + 1
            if p.count - c_count >= 0:
                cart.count += 1
                cart.unit_price = p.price
                cart.total_price += cart.unit_price
                cart.save()
            else:
                return HttpResponse("out of num")
        except Cart.DoesNotExist:
            c = Cart()
            if p.count > 0:
                c.count += 1
                c.unit_price = p.price
                c.total_price += c.unit_price
            c.id_user = user
            c.id_product = p
            c.save()
        cart = Cart.objects.filter(id_user=user)
        if cart.count() > 0:
            for c in cart:
                pro_dict.update({c.id_product.id: [c.id_product.ProductName, c.count, c.total_price]})
    return JsonResponse(pro_dict, json_dumps_params={'ensure_ascii': False}, safe=True)


def delete_api_cart(req):
    pro_dict = {}
    if req.method == "POST":
        id_cart = req.POST.get("id_cart", 0)
        user_id = req.POST.get("user_id", 0)
        try:
            id_cart = int(id_cart)
        except (ValueError, TypeError, SyntaxError):
            return JsonResponse(pro_dict, json_dumps_params={'ensure_ascii': False}, safe=True)
        if not id_cart or id_cart <= 0:
            return JsonResponse(pro_dict, json_dumps_params={'ensure_ascii': False}, safe=True)
        if user_id:
            from django.contrib.auth.models import User
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                print("User.DoesNotExist")
                return JsonResponse(pro_dict, json_dumps_params={'ensure_ascii': False}, safe=True)
        else:
            print("user_id bug")
            return JsonResponse(pro_dict, json_dumps_params={'ensure_ascii': False}, safe=True)
        from .models import Cart
        cart = Cart.objects.get(id_user=user , id=id_cart)
        if cart.count > 0:
            cart.delete()
            pro_dict = Cart.objects.filter(id_user=user)
        elif cart.count <= 0:
            return JsonResponse(pro_dict, json_dumps_params={'ensure_ascii': False}, safe=False)
    return JsonResponse(pro_dict, json_dumps_params={'ensure_ascii': False}, safe=False)



def delete_api_cart_input(req):
    pro_dict = {}
    if req.method == "POST":
        id_pro = req.POST.get("id_pro", 0)
        user_id = req.POST.get("user_id", 0)
        try:
            id_pro = int(id_pro)
        except (ValueError, TypeError, SyntaxError):
            return JsonResponse(pro_dict, json_dumps_params={'ensure_ascii': False}, safe=True)
        if not id_pro or id_pro <= 0:
            return JsonResponse(pro_dict, json_dumps_params={'ensure_ascii': False}, safe=True)
        if user_id:
            from django.contrib.auth.models import User
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                print("User.DoesNotExist")
                return JsonResponse(pro_dict, json_dumps_params={'ensure_ascii': False}, safe=True)
        else:
            print("user_id bug")
            return JsonResponse(pro_dict, json_dumps_params={'ensure_ascii': False}, safe=True)
        from .models import Cart
        cart = Cart.objects.get(id_user=user , id_product=id_pro)
        cart.total_price -= cart.unit_price
        cart.count -= 1
        cart.save()
        if cart.count > 0:
            cart = Cart.objects.filter(id_user=user)
            for c in cart:
                pro_dict.update({c.id_product.id: [c.id_product.ProductName, c.count, c.total_price]})
        elif cart.count <= 0:
            cart.delete()
            return JsonResponse(pro_dict, json_dumps_params={'ensure_ascii': False}, safe=True)
    return JsonResponse(pro_dict, json_dumps_params={'ensure_ascii': False}, safe=True)



