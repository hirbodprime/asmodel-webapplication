from django.contrib import admin

from .models import WishModel
class WishListModelAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Infomation Wishlist:',{'fields':['id_product','id_user' , 'count']}),
        ('prices:',{'fields':[ 'unit_price']}),
        ('Importants', {'fields':['controller']}),
    ]
    list_display=['id_product','id_user' ]
    search_fields=['id_product']

# Register your models here.
admin.site.register(WishModel , WishListModelAdmin)