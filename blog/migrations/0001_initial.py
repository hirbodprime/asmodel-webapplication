# Generated by Django 4.0.3 on 2022-03-23 17:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BlogTitle', models.CharField(max_length=200)),
                ('BlogImage', models.ImageField(upload_to='%Y/%m/%d')),
                ('Blog_Created_At', models.DateTimeField(auto_now_add=True)),
                ('Blog_Updated_At', models.DateTimeField(auto_now=True)),
                ('BlogBody', models.TextField(max_length=1200)),
                ('BlogBody2', models.TextField(max_length=1600)),
                ('Blogquote', models.TextField(max_length=400)),
                ('vip', models.BooleanField(blank=True, default=False, null=True)),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ModelComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('content', models.TextField(max_length=1000)),
                ('commentposted', models.DateTimeField(auto_now_add=True)),
                ('accepted', models.BooleanField(default=False)),
                ('motherpost', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.blogmodel')),
            ],
        ),
    ]