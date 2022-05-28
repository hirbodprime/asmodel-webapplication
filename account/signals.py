from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.forms import ValidationError

def updateUser(sender, instance, **kwargs):
    user = instance
    if user.first_name == '':
        user.first_name = user.username


    if len(user.username) >= 10 and user.last_name == '':
        user_last_name = user.username.split(user.username[:5])
        print(user_last_name)
        user.last_name = user_last_name[1]
    # try:
    #     validate_email(user.email)
    # except ValidationError as e:
    #     raise ValidationError('email is not safe' , e)

pre_save.connect(updateUser, sender=User)