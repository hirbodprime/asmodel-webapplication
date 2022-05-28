from django.urls import path , re_path 
from .views import LogoutView ,profileview , login_page  , registerclass , activate  , register_page
from django.contrib.auth import views as auth_views
urlpatterns = [
    
    path('profile/' , profileview , name="profileview"),
    path('logout/' , LogoutView , name="logoutview"),
    path('login/' , login_page , name="loginview"),
    path('register/' , register_page , name="registerview"),
    # path('register/' , registerclass.as_view() , name="registerview"),
    # path('register/<uidb64>/<token>', activate, name='activate'),
    # path('reset_password/', auth_views.PasswordResetView.as_view(template_name="account/password_reset.html") ,name = "reset_password"),
    # path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="account/password_reset_sent.html"),name="password_reset_done"),
    # path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset_form.html"), name="password_reset_confirm"),
    # path('reset_password_comeplete/', auth_views.PasswordResetCompleteView.as_view(template_name="account/password_reset_done.html") , name="password_reset_complete"),
    
]

