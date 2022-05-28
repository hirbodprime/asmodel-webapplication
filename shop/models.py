from django.db import models
import os
import random
from django.contrib.auth.models import User
from django_resized import ResizedImageField

# choicess = (
#     (0, 'COLORLESS'),
#     (1, 'RED'),
#     (2, 'BLUE'),
#     (3, 'BLACK'),
#     (4, 'WHITE'),
#     (5, 'GRAY'),
#     (6, 'GOLD')
#     )


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_name = random.randint(1, 27634723542)
    name, ext = get_filename_ext(filename)
    # final_name = f"{new_name}{ext}"
    final_name = f"{new_name}-{instance.ProductName}{ext}"
    return f"products/{final_name}"


class categories(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام")
    image = ResizedImageField(upload_to = 'MainCategories', verbose_name="عکس")
    def __str__(self):
        return self.name

class subcategories(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام")
    parent = models.ForeignKey(categories,on_delete=models.CASCADE, verbose_name="دسته بندی پدر")
    def __str__(self):
        return f' دسته بندی : {self.parent}   زیر دسته بندی :‌ {self.name}'
        #return self.name
    def some(self):
        return self.name 


class productmodel(models.Model):
    Seller = models.ForeignKey(User , on_delete=models.CASCADE , null=True , blank=True , verbose_name="فروشنده") 
    ProductName = models.CharField(max_length=60, verbose_name="نام محصول")
    ProductBody = models.TextField(max_length=800, verbose_name="توضیحات محصول ۱")
    ProductBody2  = models.TextField(blank=True, max_length=300, null=True, verbose_name="توضیحات محصول ۲")
    # ProductTag = models.CharField(blank=True, max_length=200, null=True)
    image = ResizedImageField(upload_to = upload_image_path , verbose_name="عکس ۱")
    image2 = models.ImageField(upload_to = upload_image_path , null=True , blank=True, verbose_name="عکس ۲")
    image3 = models.ImageField(upload_to = upload_image_path , null=True , blank=True, verbose_name="عکس ۳")
    image4 = models.ImageField(upload_to = upload_image_path , null=True , blank=True, verbose_name="عکس ۴")
    image5 = models.ImageField(upload_to = upload_image_path , null=True , blank=True, verbose_name="عکس ۵")
    # price = models.DecimalField(max_digits=12 , decimal_places=2,null=True , blank=True)
    price = models.PositiveBigIntegerField(verbose_name="قیمت")
    date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ")
    category = models.ForeignKey(subcategories , on_delete=models.CASCADE,null=True , blank=True, verbose_name="زیر دسته بندی")
    categoryMain = models.ForeignKey(categories ,blank=True, null=True, on_delete=models.CASCADE, verbose_name="دسته بندی")
    count = models.PositiveIntegerField(default=0 , verbose_name="تعداد")
    deleted = models.BooleanField(default=False, verbose_name="پاک شده")
    # color = models.PositiveSmallIntegerField(choices=choicess , default=4, verbose_name="رنگ")
    firstpage = models.BooleanField(null=True , blank=True , default=False, verbose_name="صفحه اول")
    show_price = models.CharField(default="0", blank=True, max_length=500, verbose_name="قیمت تکه شده")
    def __str__(self):
        # return f'ProuctName:{self.ProductName} ProductAuthor:{self.author} ProductId:{self.id}'
        return self.ProductName
    def getsnippet(self):
        return self.ProductBody[0:30]


class ModelCommentProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True , null=True )
    name = models.CharField(max_length=200 , blank=True , null=True, verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    content = models.TextField(max_length=1000, verbose_name="توضیح")
    commentposted = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False, verbose_name="کامنت پست بشود؟")
    motherpost = models.ForeignKey(productmodel , on_delete=models.CASCADE, blank=True , null=True, verbose_name="پست مادر")
    def __str__(self):
        return f'محصول مادر: {self.motherpost} '