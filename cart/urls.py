from django.urls import path , include
from .views import CarTpageView ,  add_api_cart , get_mycart , delete_api_cart , delete_api_cart_input 

urlpatterns = [
    path('', CarTpageView, name="cartview"),
    path('add_api', add_api_cart, name="add_api_cart"),
    path('get_mycart', get_mycart, name="get_mycart"),
    path('delete_cart_pro' , delete_api_cart , name="delete_api_cart"),
    path('delete_api_cart_input' , delete_api_cart_input , name="delete_api_cart_input") ,
    ]
