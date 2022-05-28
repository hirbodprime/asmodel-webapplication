from .models import productmodel , subcategories , categories 
from cart.models import Cart 
from wishlist.models import WishModel
# sube = subcategories.objects.only('name')
# print(sube)
# for i in sube:
#     pe = productmodel.objects.filter(category = i).categoryMain.all()
#     print(pe)
pro1 = productmodel.objects.filter(category=1, deleted=False)
# pro2 = productmodel.objects.filter(category=2)
pro3 = productmodel.objects.filter(category=3 , deleted=False)
pro4 = productmodel.objects.filter(category=4, deleted=False) 
# pro5 = productmodel.objects.filter(category=5)
# pro6 = productmodel.objects.filter(category=6)
# pro7 = productmodel.objects.filter(category=7) 
pro8 = productmodel.objects.filter(category=8, deleted=False)
# pro9 = productmodel.objects.filter(category=9)
# pro10 = productmodel.objects.filter(category=10) 
# pro11 = productmodel.objects.filter(category=11)
# pro12 = productmodel.objects.filter(category=12)
# pro13 = productmodel.objects.filter(category=13)
# pro14 = productmodel.objects.filter(category=14)
# pro15 = productmodel.objects.filter(category=15)
# pro16 = productmodel.objects.filter(category=16)
# pro17 = productmodel.objects.filter(category=17)
# pro18 = productmodel.objects.filter(category=18)
# pro19 = productmodel.objects.filter(category=19)
# pro20 = productmodel.objects.filter(category=20)
# pro21 = productmodel.objects.filter(category=21)
# pro22 = productmodel.objects.filter(category=22)
# pro23 = productmodel.objects.filter(category=23)
# pro24 = productmodel.objects.filter(category=24)
# pro25 = productmodel.objects.filter(category=25)
# pro26 = productmodel.objects.filter(category=26)
# pro27 = productmodel.objects.filter(category=27)
pro = productmodel.objects.filter(deleted=False)
cate = categories.objects.all()
subcat = subcategories.objects.all()


def GlobalModels(request):
    user = request.user
    if user.is_authenticated:
        cart = Cart.objects.filter(id_user=user)
        c_count = 0
        pro_list = []
        total_price = 0
        # ca = cart.count()
        wishe = WishModel.objects.filter(id_user=user)
        w = wishe.count()
        for i in cart:
            pro_list.append([i.id_product.ProductName, i.id_product.image, i.count, i.unit_price, i.total_price, i.id_product.id , i.id])
            total_price += i.total_price
            c_count += i.count
        return { 
                    "cart": pro_list,"total_price": total_price,"ca":c_count,
                    'cat':cate , 'sub': subcat ,  'pro':pro,
                    'pro4':pro4, 'pro8':pro8 ,'pro1':pro1,'pro3':pro3, 'w':w
            }
    return {
        'cat':cate , 'sub': subcat , 'pro':pro,
        'pro4':pro4, 'pro8':pro8 ,'pro1':pro1,'pro3':pro3,
        
    }
        # 'pro2':pro2 , 'pro3':pro3 ,'pro10':pro10
        # 'pro8':pro8,'pro9':pro9  ,'pro6':pro6,
        # 'pro11':pro11 , 'pro12':pro12,
        # 'pro13':pro13 ,'pro14':pro14 , 'pro15':pro15 , 'pro16':pro16,
        # 'pro17':pro17,'pro18':pro18 ,'pro19':pro19, 'pro20':pro20 ,
        # 'pro21':pro21,'pro22':pro22 ,'pro23':pro23 , 'pro24':pro24 , 'pro24':pro24,
        # 'pro25':pro25 ,'pro26':pro26 , 'pro27':pro27
