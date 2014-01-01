from django.db import models
from django import forms
from django.conf import settings

from djangoratings.fields import RatingField
from sorl.thumbnail import ImageField
from sorl.thumbnail import get_thumbnail
from django.core.files.base import ContentFile

from coffee_bag.models import PurchasedCoffeeBag

def upload_to_cmaker(instance):
        return '%s/cmaker' % (instance.user.username)
    
def upload_to_cgrinder(instance):
        return '%s/cgrinder' % (instance.user.username)
    
def upload_to_preps(instance):
    return '%s/preps' % (instance.user.username)


class Method(models.Model):
    """DB model for a preparation method.
    
    """
    
    name = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    rec_grind = models.CharField(max_length=100, blank=True, null=True)
    rec_water_amt = models.IntegerField(blank=True, null=True)
    rec_coffee_amt = models.IntegerField(blank=True, null=True)
    rec_temp = models.FloatField(blank=True, null=True) 
    
    thumb = ImageField(upload_to='method/', blank=True, null=True)

    def __unicode__(self):
        return self.name

class CoffeeMaker(models.Model):
    """DB model for a generic type of coffee maker.
    
    """

    name = models.CharField(max_length=500)
    manufacturer = models.CharField(max_length=500)
    model = models.CharField(max_length=500)
    volume = models.FloatField(blank=True, null=True)
    
    description = models.TextField(blank=True, null=True)
        
    rating = RatingField(range=5, weight=5, can_change_vote=True, allow_delete=True, allow_anonymous=False)

    method = models.OneToOneField(Method)    
 

class CoffeeMakerImage(models.Model):
    """DB model for coffee maker images (to allow multiple images).

    """
    image = models.ImageField(upload_to=upload_to_cmaker, blank = True, null = True)
    caption = models.CharField(max_length = 250, blank =True, null = True)
        
    coffee_maker = models.ForeignKey(CoffeeMaker)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)
        
    def save(self, *args, **kwargs):
        if not self.id:  
            super(CoffeeMakerImage, self).save(*args, **kwargs)  
            resized = get_thumbnail(self.image, "250x250", crop='center', quality=99) 
            self.image.save(resized.name, ContentFile(resized.read()), True)
        super(CoffeeMakerImage, self).save(*args, **kwargs)
        
    class Meta:
        permissions = (('view_coffee_maker_image', "View coffee maker image"),)
 
 
class PurchasedCoffeeMaker(models.Model):
    """DB model for a type of coffee maker that a user has.
    
    For example, it may be a different model, size, etc.
    
    """

    # should be changed to only a year
    date_purch = models.DateField('Purchase Date', blank=True)
    rating = RatingField(range=5, weight=5, can_change_vote = True, allow_delete = True, allow_anonymous = False)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)    
    coffeemaker = models.ForeignKey(CoffeeMaker)
    
    thumb = models.ForeignKey(CoffeeMakerImage, null=True, blank=True)
    
    notes = models.TextField(blank=True, null=True)

    
    class Meta:
        # Default ordering - chronological by purchase date
        ordering = ["-date_purch"]

        permissions = (('view_purch_coffee_maker', 'View purchased coffee maker'),)
    
   
class CoffeeGrinder(models.Model):
    """DB model for a coffee grinder.
    
    """

    name = models.CharField(max_length=500)
    manufacturer = models.CharField(max_length=500)
    model = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)    
    rating = RatingField(range=5, weight=5, can_change_vote=True, allow_delete=True, allow_anonymous=False)

    def __unicode__(self):
        return self.name
    
   
class CoffeeGrinderImage(models.Model):
    """DB model for coffee maker images (to allow multiple images).

    """
    image = models.ImageField(upload_to=upload_to_cgrinder, blank = True, null = True)
    caption = models.CharField(max_length = 250, blank =True, null = True)
        
    coffee_grinder = models.ForeignKey(CoffeeGrinder)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)
        
    def save(self, *args, **kwargs):
        if not self.id:  
            super(CoffeeGrinderImage, self).save(*args, **kwargs)  
            resized = get_thumbnail(self.image, "250x250", crop='center', quality=99) 
            self.image.save(resized.name, ContentFile(resized.read()), True)
        super(CoffeeGrinderImage, self).save(*args, **kwargs)
        
    class Meta:
        permissions = (('view_coffee_grinder_image', "View coffee grinder image"),)
        
        
class PurchasedCoffeeGrinder(models.Model):
    """DB model for a type of coffee maker that a user has.
    
    For example, it may be a different model, size, etc.
    
    """

    # should be changed to only a year
    date_purch = models.DateField('Purchase Date', blank=True)
    rating = RatingField(range=5, weight=5, can_change_vote = True, allow_delete = True, allow_anonymous = False)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)    
    coffeegrinder = models.ForeignKey(CoffeeGrinder)
    
    notes = models.TextField(blank=True, null=True)
    
    thumb = models.ForeignKey(CoffeeGrinderImage, null=True, blank=True)

    def __unicode__(self):
        return self.coffeegrinder.name
    
    class Meta:
        # Default ordering - chronological by purchase date
        ordering = ["-date_purch"]

        permissions = (('view_purch_coffee_grinder', 'View purchased coffee grinder'),)


class CoffeePrepImage(models.Model):
    """DB model for coffee maker images (to allow multiple images).

    """
    image = models.ImageField(upload_to=upload_to_preps, blank = True, null = True)
    caption = models.CharField(max_length = 250, blank =True, null = True)
    
    method = models.ForeignKey(PurchasedCoffeeMaker)
    coffeebag = models.ForeignKey(PurchasedCoffeeBag)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
        
    def save(self, *args, **kwargs):
        if not self.id:  
            super(CoffeePrepImage, self).save(*args, **kwargs)  
            resized = get_thumbnail(self.image, "250x250", crop='center', quality=99) 
            self.image.save(resized.name, ContentFile(resized.read()), True)
        super(CoffeePrepImage, self).save(*args, **kwargs)
        
    class Meta:
        permissions = (('view_coffee_preparation_image', "View coffee preparation image"),)
        
    
class Preparation(models.Model):
    """DB model for a coffee preparation.

    Includes all variables, equipment, and coffee involved in making a coffee.
    
    Has relationships to a method, grinder, purchased coffee bag, and a user.
    
    """

    date = models.DateField('Preparation Date', blank=True)

    grind = models.CharField(max_length=100, blank=True, null=True)
    water_amt = models.IntegerField(blank=True, null=True)
    coffee_amt = models.IntegerField(blank=True, null=True)
    time_amt = models.IntegerField(blank=True, null=True)
    extraction = models.FloatField(blank=True, null=True)

    # Total dissolved solids
    tds = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    
    notes = models.TextField(blank=True, null=True)
    
    rating_taste = RatingField(range=5, weight=5, can_change_vote = True, allow_delete = True, allow_anonymous = False)
    rating_aroma = RatingField(range=5, weight=5, can_change_vote = True, allow_delete = True, allow_anonymous = False)
    rating_tactile = RatingField(range=5, weight=5, can_change_vote = True, allow_delete = True, allow_anonymous = False)

    method = models.ForeignKey(Method)
    grinder = models.ForeignKey(PurchasedCoffeeGrinder, null=True, blank=True)
    coffeebag = models.ForeignKey(PurchasedCoffeeBag)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    
    thumb = models.ForeignKey(CoffeePrepImage, null=True, blank=True)
    
    def __unicode__(self):
	    return "%s, %s on %s by %s" % (self.coffeebag.coffeebag.coffee.name, self.method, self.date, self.user)

    class Meta:
        # Default ordering - chronological by purchase date
        ordering = ["-date"]

        permissions = (('view_preparation', 'View preparation'),)

    
    ## tags for flavor notes?
    # tags = sometaggingappmodel()
    
    ## Need to investigate how to share b/t users...
