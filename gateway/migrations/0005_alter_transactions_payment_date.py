# Generated by Django 4.0.3 on 2022-04-19 05:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0004_alter_transactions_payment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='payment_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 19, 10, 17, 4, 567727), verbose_name='تاریخ پرداخت'),
        ),
    ]
