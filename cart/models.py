from django.db import models
from shop.models import productmodel
from django.contrib.auth.models import User
# Create your models here.
class BaseModel(models.Model):
    id_product = models.ForeignKey(productmodel, verbose_name="نام محصول", on_delete=models.CASCADE, blank=True)
    id_user = models.ForeignKey(User, verbose_name="نام کاربری", on_delete=models.CASCADE, blank=True)
    count = models.PositiveIntegerField(default=0, blank=True, verbose_name="تعداد")
    unit_price = models.PositiveBigIntegerField(verbose_name="مبلغ واحد" , blank=True,default=0)
    class Meta:
        abstract = True

class Cart(BaseModel):
    total_price = models.PositiveIntegerField(verbose_name="مبلغ نهایی" , blank=True ,default=0)
    deleted = models.BooleanField(default=False , blank=True)
