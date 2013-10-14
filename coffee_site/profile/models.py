from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
from django.conf import settings
from django.core.files.base import ContentFile

from sorl.thumbnail import ImageField
from sorl.thumbnail import get_thumbnail

def upload_to_user(instance, name):
    return '%s/%s' % (instance.username, name)

class CoffeeUser(AbstractUser):
    """Subclass user to add extra fields.
    
    """
    
    facebook  = models.CharField(max_length=500, blank=True, null=True)
    twitter  = models.CharField(max_length=500, blank=True, null=True)
    gplus  = models.CharField(max_length=500, blank=True, null=True)

    skill_level = models.CharField(max_length=1, choices=(('B', 'Beginner'), ('I', 'Intermediate'), ('A', 'Advanced'), ('I', 'Professional')), null=True, blank=True)

    avatar = ImageField(upload_to=upload_to_user, blank=True, null=True)
    
    date_birth = models.DateField('Date of birth', blank=True, null=True)    
    sex = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), null=True, blank=True)
    
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
        
    def save(self, *args, **kwargs):
        if not self.pk:
        #super(CoffeeUser, self).save(*args, **kwargs)  
            resized = get_thumbnail(self.avatar, '250x250', crop='center', quality=99)
            self.avatar.save(resized.name, ContentFile(resized.read()), True)
        super(CoffeeUser, self).save(*args, **kwargs)
        