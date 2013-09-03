from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
from django.conf import settings

class CoffeeUser(AbstractUser):
    """Subclass user to add extra fields.

    Only extra fields now are to determine what objects (purchased coffee bags
    and ratio preparations for now) the user wants to share.

    """
    
    facebook  = models.CharField(max_length=500, blank=True, null=True)
    twitter  = models.CharField(max_length=500, blank=True, null=True)
    gplus  = models.CharField(max_length=500, blank=True, null=True)

    skill_level = models.CharField(max_length=500, blank=True, null=True)

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
    
