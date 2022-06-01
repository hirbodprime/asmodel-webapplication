from django.dispatch import receiver
from django.db.models.signals import pre_save , post_save
from django.utils.text import slugify
from .models import BlogModel

# @receiver(post_save , sender=BlogModel)
def slogify(sender , instance ,created , *args, **kwargs):
    if created:
        print("am i here?")
        sluge = slugify(instance.BlogTitle)
        # exist = BlogModel.objects.filter(slug=slug).exists()
        # if exists:
        #     slug = "%s-%s" %(slug , instance.id)
        ide = str(instance.id)
        slug = sluge +"-"+ ide
        instance.slug = slug
        instance.save()
    # elif not created:
    #     print('hibord')
    # else:
    #     print('hihihihihihihihihihihihi')
post_save.connect(slogify , sender=BlogModel)

# @receiver(pre_save , sender=BlogModel)
def slogify(sender , instance  , *args, **kwargs):
    if not instance.slug:
        print('fuck all coders')
        slug = slugify(instance.BlogTitle)
        if instance.id:
            ide = str(instance.id)
            slug = slug +"-"+ ide
            instance.slug = slug
        else:
            print('jorboze nadari binamos')
            # instance.slug = slug
    else:
        print("do nothing")
pre_save.connect(slogify , sender=BlogModel)
