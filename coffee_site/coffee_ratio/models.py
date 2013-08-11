from django.db import models
from django.contrib.auth.models import User
from django import forms

from djangoratings.fields import RatingField
from sorl.thumbnail import ImageField

from coffee_bag.models import PurchasedCoffeeBag

class Method(models.Model):
    """DB model for a preparation method.
    
    """
    
    name = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    thumb = ImageField(upload_to='/media/img/', blank=True)
    rec_grind = models.CharField(max_length=100, blank=True, null=True)
    rec_water_amt = models.IntegerField(blank=True, null=True)
    rec_coffee_amt = models.IntegerField(blank=True, null=True)
      
    
class CoffeeMaker(models.Model):
    """DB model for a generic type of coffee maker.
    
    """

    name = models.CharField(max_length=500)
    manufacturer = models.CharField(max_length=500)
    model = models.CharField(max_length=500)
    volume = models.FloatField(blank=True, null=True)
    
    description = models.TextField(blank=True, null=True)
    thumb = ImageField(upload_to='/media/img/', blank=True)

    method = models.OneToOneField(Method)    
    
class CoffeeGrinder(models.Model):
    """DB model for a coffee grinder.
    
    """

    name = models.CharField(max_length=500)
    manufacturer = models.CharField(max_length=500)
    model = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    thumb = ImageField(upload_to='/media/img/', blank=True)
    
class PurchasedCoffeeMaker(models.Model):
    """DB model for a type of coffee maker that a user has.
    
    For example, it may be a different model, size, etc.
    
    """

    # should be changed to only a year
    date_purch = models.DateField('Purchase Date', blank=True)
    rating = RatingField(range=5)
    user = models.ManyToManyField(User)    
    coffeemaker = models.ForeignKey(CoffeeMaker)


class PurchasedCoffeeGrinder(models.Model):
    """DB model for a type of coffee maker that a user has.
    
    For example, it may be a different model, size, etc.
    
    """

    # should be changed to only a year
    date_purch = models.DateField('Purchase Date', blank=True)
    rating = RatingField(range=5)
    user = models.ManyToManyField(User)    
    coffeegrinder = models.ForeignKey(CoffeeGrinder)
    
    
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
    notes = models.TextField(blank=True, null=True)
    rating = RatingField(range=5)

    method = models.ForeignKey(PurchasedCoffeeMaker)
    grinder = models.ForeignKey(PurchasedCoffeeGrinder)
    coffeebag = models.ForeignKey(PurchasedCoffeeBag)
    user = models.ForeignKey(User)
    
    ## tags for flavor notes?
    # tags = sometaggingappmodel()
    
    ## Need to investigate how to share b/t users...
