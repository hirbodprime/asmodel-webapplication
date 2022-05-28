from django.contrib import admin
from .models import productmodel , subcategories , categories , ModelCommentProduct
# Register your models here.
class ProductModeladmin(admin.ModelAdmin):
    fieldsets = [
        ('ProductName&Seller' , {'fields':['ProductName' , 'Seller' ]}),
        ('ProductImage' , {'fields':['image' , 'image2', 'image3', 'image4', 'image5']}),
        ('ProductInformation' , {'fields':['ProductBody' , 'ProductBody2' , 'price' , 'show_price' , 'count' ,'categoryMain' , 'category','deleted' , 'firstpage']})
    ]
    list_display= ['ProductName','deleted','id' ,  'Seller' , 'date' , 'category' , 'categoryMain']
    search_fields=['id']

    
class categoriesAdmin(admin.ModelAdmin):
    list_display= [ 'name' , 'id']
class subcategoriesAdmin(admin.ModelAdmin):
    list_display= ['parent','id' , 'name' ]
    search_fields=['name']

admin.site.register(ModelCommentProduct)
admin.site.register(productmodel ,ProductModeladmin)
admin.site.register(subcategories , subcategoriesAdmin)
admin.site.register(categories , categoriesAdmin)