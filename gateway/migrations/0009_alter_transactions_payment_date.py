# Generated by Django 4.0.3 on 2022-06-01 08:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0008_alter_transactions_payment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='payment_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 1, 12, 54, 55, 616656), verbose_name='تاریخ پرداخت'),
        ),
    ]
