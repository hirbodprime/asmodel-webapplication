from django.urls import path 
from .views import  ProductDetailsView , ProShopView , categoryView , subproshopview , commentView , TabProducts2 , index , number_seprator
urlpatterns = [

    path('', index, name="shopview"),
    path('<int:page>', TabProducts2, name="tabviewname2"),
    path('number_sep2022/',number_seprator, name="number_seprator"),
    path('<str:categoriese>/' , categoryView , name="ProShopView2"),
    path('<str:subename>' , subproshopview , name="subproshopview"),
    path('products/<str:namepro>/' , ProductDetailsView , name="productview"),
    path('products/<str:proname>/comment/' , commentView , name="commentviewshop"),
    path('<str:namemain>/<str:subname>/' , ProShopView , name="ProShopView"),

]
