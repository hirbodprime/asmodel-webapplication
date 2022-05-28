from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('home.urls')),
    path('account/' , include('account.urls')),
    path('shop/' , include('shop.urls')),
    path('blog/' , include('blog.urls')),
    path('cart-list/' , include('cart.urls')),
    path('wishlist/' , include('wishlist.urls')),
    path('gateway/', include("gateway.urls"))

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
