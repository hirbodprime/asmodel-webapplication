from django.db import models

# Create your models here.
# from django.db.models import Model
import datetime

from django.contrib.auth import get_user_model

state_payment = (
    (0, "پرداخت ناموفق"),
    (1, "پرداخت موفق"),
    (2, "در انتظار پرداخت")
)


class Transactions(models.Model):
    # id = models.IntegerField(primary_key=True, unique=True)
    authority = models.CharField(max_length=40, verbose_name="کد تراکنش")
    payment_date = models.DateTimeField(blank=True, default=datetime.datetime.now(),verbose_name="تاریخ پرداخت")
    state = models.IntegerField(choices=state_payment, default=2, verbose_name="وضعیت تراکنش")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    ref_id = models.CharField(max_length=20, default="", blank=True, verbose_name="کد پیگیری")
    amount = models.IntegerField(default=0, blank=True, verbose_name="مبلغ پرداخت")

    class Meta:
        verbose_name = "جدول تراکنش"