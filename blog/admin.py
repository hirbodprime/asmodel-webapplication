from django.contrib import admin
from .models import BlogModel , ModelComment

# Register your models here.
class BlogModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(BlogModel , BlogModelAdmin)

admin.site.register(ModelComment)
