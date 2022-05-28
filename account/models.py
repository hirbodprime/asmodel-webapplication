from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# gender = (
#     (0 , 'بدون جنسیت'),
#     (1 , 'آقا'),
#     (2 , 'خانم'),
#     (3 , 'دیگر'),
# )

# class profilemodel(models.Model):
#     username = models.ForeignKey(User , on_delete=models.CASCADE)
#     phone = PhoneNumberField(null=False, blank=False, unique=True)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     picture = models.ImageField(upload_to="profile_pics")
#     gender = models.PositiveSmallIntegerField(default=0 ,null=True) 

# from django.core.validators import RegexValidator
# class Person(models.Model):
#     phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
#     phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)

