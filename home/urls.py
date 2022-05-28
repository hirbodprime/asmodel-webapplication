from django.urls import path 
from .views import homeview , aboutview   , h404 , faq, coming , privacy , contactview
urlpatterns = [

    path('' , homeview , name="homeview"),
    path('contact/' , contactview , name="contactview"),
    path('about/' , aboutview , name="aboutview"),
    path('questions/' , faq , name='faq'),
    path('coming-soon/' , coming , name='com'),
    path('H404/' , h404 , name='H404'),
    path('privacy-policy/' , privacy , name='privacy'),

]
