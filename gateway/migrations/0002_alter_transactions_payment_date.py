# Generated by Django 4.0.3 on 2022-04-14 15:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='payment_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 14, 19, 43, 9, 321214), verbose_name='تاریخ پرداخت'),
        ),
    ]
