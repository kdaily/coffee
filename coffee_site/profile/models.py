from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
from django.conf import settings

from sorl.thumbnail import ImageField

def upload_to_user(instance):
    return '%s' % (instance.user.username)

class CoffeeUser(AbstractUser):
    """Subclass user to add extra fields.
    
    """
    
    facebook  = models.CharField(max_length=500, blank=True, null=True)
    twitter  = models.CharField(max_length=500, blank=True, null=True)
    gplus  = models.CharField(max_length=500, blank=True, null=True)

    skill_level = models.CharField(max_length=500, blank=True, null=True)

    avatar = ImageField(upload_to=upload_to_user, blank=True)
    
    # Encoding for sharing fields
    NOSHARE = 0
    SHAREFRIENDS = 1
    SHAREALL = 2

    # Possible choices for sharing
    SHARE_CHOICES = (
        (NOSHARE, 'No sharing'),
        (SHAREFRIENDS, 'Share with friends'),
        (SHAREALL, 'Share with everyone'),
    )

    purch_coffee_bag_sharing = models.SmallIntegerField(choices=SHARE_CHOICES,
                                                        default=NOSHARE)

    ratio_sharing = models.SmallIntegerField(choices=SHARE_CHOICES,
                                             default=NOSHARE)

    friends = models.ManyToManyField(settings.AUTH_USER_MODEL)
    
