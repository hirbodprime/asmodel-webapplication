from django.http import HttpResponse, JsonResponse
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from HirMethods.methods import num_sep
@login_required(login_url="/account/login")
def WishListView(req):
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
        from wishlist.models import WishModel
        try:
            p = productmodel.objects.get(deleted=False, id=id_pro)
        except productmodel.DoesNotExist:
            return JsonResponse(pro_dict, json_dumps_params={'ensure_ascii': False}, safe=True)
        try:
            wish = WishModel.objects.get(id_user=user, id_product=p)
            return HttpResponse("exist")
        except WishModel.DoesNotExist:
            c = WishModel()
            cont = 0
            controler = 0
            w_wish = WishModel.objects.filter(id_user=user)
            for i in w_wish:
                cont += i.count
                controler = i.controller
            if controler - cont >=0:
                c.count += 1
                c.unit_price = p.price
                c.id_user = user
                c.id_product = p
                c.save()      
                return HttpResponse('added')
            else:
                return HttpResponse('full')
    return JsonResponse(pro_dict, json_dumps_params={'ensure_ascii': False}, safe=True)


@login_required(login_url="/account/login")
def WishListpageView(request):
    from wishlist.models import WishModel
    user = request.user
    cart = WishModel.objects.filter(id_user=user)
    pro_list = []
    for i in cart:
        show_price = num_sep(i.unit_price)
        pro_list.append([i.id_product.ProductName, i.id_product.image, i.count, show_price , i.id_product.id , i.id])
    return render(request, "shop/wishlist.html", {"wish": pro_list})


@login_required(login_url="/account/login")
def delete_api_wish(req):
    pro_dict = {}
    if req.method == "POST":
        id_wish = req.POST.get("id_wish", 0)
        user_id = req.POST.get("user_id", 0)
        try:
            id_wish = int(id_wish)
        except (ValueError, TypeError, SyntaxError):
            return JsonResponse(pro_dict, json_dumps_params={'ensure_ascii': False}, safe=True)
        if not id_wish or id_wish <= 0:
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
        from .models import WishModel
        wish = WishModel.objects.get(id_user=user , id=id_wish)
        if wish.count > 0:
            wish.delete()
            pro_dict = WishModel.objects.filter(id_user=user)
        elif wish.count <= 0:
            return JsonResponse(pro_dict, json_dumps_params={'ensure_ascii': False}, safe=False)
    return JsonResponse(pro_dict, json_dumps_params={'ensure_ascii': False}, safe=False)