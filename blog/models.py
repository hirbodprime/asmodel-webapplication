from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogModel(models.Model):
    writer = models.ForeignKey(User , on_delete=models.CASCADE)
    BlogTitle = models.CharField(max_length=200)
    BlogImage = models.ImageField(upload_to ='%Y/%m/%d')
    Blog_Created_At = models.DateTimeField(auto_now_add=True)
    Blog_Updated_At = models.DateTimeField(auto_now=True)
    BlogBody  = models.TextField(max_length=1200)
    BlogBody2 = models.TextField(max_length=1600)
    Blogquote = models.TextField(max_length=400)
    vip = models.BooleanField(default=False, blank=True , null=True)
    def __str__(self):
        return self.BlogTitle
    def getsnippets(self):
        return self.BlogBody[:160]


class ModelComment(models.Model):
    name = models.CharField(max_length=200 , blank=True , null=True)
    email = models.EmailField()
    content = models.TextField(max_length=1000)
    commentposted = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    motherpost = models.ForeignKey(BlogModel , on_delete=models.CASCADE, blank=True , null=True)
    def __str__(self):
        return f'بلاگ مادر: {self.motherpost} '