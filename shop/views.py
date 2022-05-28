from django.shortcuts import render , redirect
from .models import productmodel , categories,subcategories , ModelCommentProduct
from blog.forms import CommentForm
from django.contrib.auth.decorators import login_required , user_passes_test
from django.http import HttpResponse




    
def index(request):  
    c = 8
    s = 0
    p = productmodel.objects.filter(deleted=False)
    list_of_product = []
#     در اینجا ما ار فیلد deleted = False
#     چون میخوایم محصولاتی که پاک نشدن رو بیاره تا به خطا بر نخوریم
    n = 0
    for i in p:
        n += 1
        if s < n < c:
            # در اینجا چون ما از  and  استفاده کردیم باید هردو شرط درست باشه به همین دلیل
            # ما برابر c در elif قرار دادیم
                                                # 0                  1    2         3          4         5                6             7            8             9                10                  
            list_of_product.append([i.ProductName , i.id , i.image , i.image2, i.show_price , i.ProductBody , i.ProductBody2 , i.count , i.getsnippet ,i.categoryMain ,i.category.some])
        elif n == c:
            list_of_product.append([i.ProductName , i.id , i.image , i.image2, i.show_price , i.ProductBody , i.ProductBody2 , i.count , i.getsnippet ,i.categoryMain ,i.category.some])
            break

    cate = list(categories.objects.all())

    max = list(productmodel.objects.all())
    max = (len(max) // 10) + 1
    
    n_page = list(range(1, max + 1, 1))
    befor = 1
    after = 2
    # علت استفاده ار لیست اینکه خروجی all()
    # به صورت آبجکتی ار تمام اون موارد خواسته شده هستش و اینجا میشه تمام دسته بندی مادر
    # به همین دلیل از متد لیست برای تبدیل اون آیجکت به لیست استفاده کردیم
    c = []
    # dict_c= {}
    for i in cate:
        c.append([i.id, i.name])
        # c.append({"id": i.id, "name":i.name})

    return render(request, "shop/shop2.html", {"list": list_of_product, "category": c, "page": n_page,
                                                    "befor": befor, "after": after, "loc_page": 1, "max": max})



def TabProducts2(req, page):
    listPro = []
    try:
        num = int(page)
    except (ValueError, TypeError, SyntaxError):
        return HttpResponse("عدد وارد کنید")
    max = list(productmodel.objects.all())
    max = (len(max) // 10) + 1
    n_page = list(range(1, max+1, 1))
    if page > max:
        num = max
        page = max

    if num == 1:
        c = 8 * num
        s = 0
        befor = 1
        after = num + 1
    else:
        c = 8 * num
        s = 8 * (num-1)
        befor = num - 1
        after = num + 1
    pro = productmodel.objects.filter(deleted=False)

    n = 0
    for i in pro:
        n += 1
        if s < n < c:
            listPro.append([i.ProductName , i.id , i.image , i.image2, i.show_price , i.ProductBody , i.ProductBody2 , i.count , i.getsnippet ,i.categoryMain ,i.category.some])
        elif n == c:
            listPro.append([i.ProductName , i.id , i.image , i.image2, i.show_price , i.ProductBody , i.ProductBody2 , i.count , i.getsnippet ,i.categoryMain ,i.category.some])
            break
    return render(req, 'shop/shop2.html', {"list": listPro, "page": n_page, "befor": befor,
                                                "after": after, "loc_page": page, "max": max})





def ProductDetailsView(req , namepro):
    pro = productmodel.objects.get(ProductName = namepro)
    p_price = pro.price
    commentobject = ModelCommentProduct.objects.filter(accepted = True , motherpost = pro)
    comment_count = commentobject.count()
    return render(req , 'shop/product-details.html' , {'p':pro , 'com':commentobject , 'c_count':comment_count})

def subproshopview(req , subename):
    if subcategories.objects.filter(name = subename):
        sub = subcategories.objects.filter(name = subename)
        for i in sub:
            o = i.id
            pro = productmodel.objects.filter(category = o, deleted=False)
            return render(req , 'shop/shop.html' , {'pro':pro} )
    else:
        return redirect("H404")



def ProShopView(req ,namemain,  subname):
    if subcategories.objects.filter(name = subname) and categories.objects.get(name=namemain):
        cat = categories.objects.get(name = namemain)
        sub = subcategories.objects.filter(name = subname)
        n = cat.id
        for i in sub:
            o = i.id
            if productmodel.objects.filter(category = o , categoryMain=n):
                pro = productmodel.objects.filter(category = o , categoryMain=n , deleted=False)
                return render(req , 'shop/shop.html' , {'pro':pro} )
    else:
        return redirect("H404")


def categoryView(req , categoriese):
    if categories.objects.filter(name = categoriese):
        cat = categories.objects.filter(name = categoriese)
        for i in cat:
            o = i.id
            pro = productmodel.objects.filter(categoryMain = o, deleted=False)
            return render(req , 'shop/shop.html' , {'pro':pro} )
    else:
        return redirect("H404")

@login_required(login_url="/account/login")
def commentView(request , proname):
    user = request.user
    comment = CommentForm(request.POST or None)
    context = {"fc":comment }
    if request.method == "POST":
        if comment.is_valid():
            use = user
            name = comment.cleaned_data['name']
            email = comment.cleaned_data['email']
            content = comment.cleaned_data['content']
            pro = productmodel.objects.get(ProductName = proname)
            promother = pro
            comment = ModelCommentProduct.objects.create( user= use ,name = name,email = email , content = content , motherpost = promother )
            if comment.name and comment.email and comment.content != None:
                comment.save()
                return redirect('productview' , pro )
    return render(request, 'blog/newcomment.html' , context)



@user_passes_test(lambda u: u.is_superuser)
def number_seprator(request):
    from .models import productmodel
    import locale
    locale.setlocale(locale.LC_ALL, '')  
    p = productmodel.objects.filter(deleted=False)
    for i in p:
        id_pro = i.id
        value = i.price
        value = f'{value:n}' 
        try:
            pro = productmodel.objects.get(id=id_pro)
            pro.show_price = value
            pro.save()
        except productmodel.DoesNotExist:
            return HttpResponse(" محصول با آیدی " + id_pro + " یافت نشد ")
    return HttpResponse("همشون حل شد حاجی")