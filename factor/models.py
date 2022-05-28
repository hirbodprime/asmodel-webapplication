from django.db import models
from django.contrib.auth.models import User
from shop.models import Products
from datetime import datetime
# Create your models here.

factor_state = (
    (0, "پرداخت نشده"),
    (2, "در انتظار پرداخت"),
    (1, "پرداخت شده"),
)


class Factors(models.Model):
    id_user = models.ForeignKey(User, verbose_name="نام کاربر", on_delete=models.CASCADE)
    payment_date = models.DateTimeField(default=datetime.now(), blank=True, verbose_name="تاریخ پرداخت")
    state = models.SmallIntegerField(choices=factor_state, default=1, blank=True, verbose_name="وضعیت پرداخت")
    ref_id = models.CharField(max_length=20, default="", blank=True, verbose_name="کد پیگیری")
    creat_date = models.DateTimeField(default=datetime.now(), blank=True, verbose_name="تاریخ ایجاد فاکتور")
    total_price = models.PositiveIntegerField(verbose_name="مبلغ نهایی", blank=True, default=0)


class FacotrProduct(models.Model):
    id_factor = models.ForeignKey(Factors, verbose_name="فاکتور", on_delete=models.CASCADE)
    id_product = models.ForeignKey(Products, verbose_name="نام محصول", on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1, blank=True, verbose_name="تعداد محصول")
    unit_price = models.PositiveIntegerField(default=0, blank=True, verbose_name="قیمت واحد")
    total_price = models.PositiveIntegerField(verbose_name="مبلغ نهایی")