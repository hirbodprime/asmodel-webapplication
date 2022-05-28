from django.db import models
from cart.models import BaseModel
# Create your models here.
class WishModel(BaseModel):
    controller = models.PositiveBigIntegerField(default=15 , blank=True)