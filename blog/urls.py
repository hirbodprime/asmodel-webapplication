from django.urls import path 
from .views import BlogView , BlogDetailView , commentView

urlpatterns = [
    path('' , BlogView , name="blogview"),
    path('blog-details/<str:BlogTitle>' , BlogDetailView , name="blogdetailview"),
    path('blog-details/<str:BlogTitle>/comment' , commentView , name="commentview")
]
