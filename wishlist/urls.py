from django.urls import path 
from .views import  WishListpageView ,  WishListView , delete_api_wish

urlpatterns = [
    path('add_wish_list_api', WishListView, name="add_wish_list_api"),
    path('delete_api_wish', delete_api_wish, name="delete_api_wish"),
    path('', WishListpageView, name="wishlistview")
    ]
