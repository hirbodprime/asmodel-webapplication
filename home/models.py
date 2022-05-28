from django.db import models
from django.db import models


class ModelContact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    title = models.CharField(max_length=300)
    content = models.TextField(max_length=1000)