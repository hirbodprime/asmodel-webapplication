from django.contrib import admin
from .models import ModelContact 

class ModelContactAdmin(admin.ModelAdmin):
    list_display=['name' , 'email' , 'title' , 'content']


admin.site.register(ModelContact , ModelContactAdmin)

