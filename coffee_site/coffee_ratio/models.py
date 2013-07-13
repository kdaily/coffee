from django.db import models
from django.contrib.auth.models import User
from django import forms

from djangoratings.fields import RatingField
from sorl.thumbnail import ImageField

from base.models import Coffee, PurchasedCoffeeBag

class Method(models.Model):

    name = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    thumb = ImageField(upload_to='/media/img/', blank=True)
    rec_grind = models.CharField(max_length=100, blank=True, null=True)
    rec_water_amt = models.IntegerField(blank=True, null=True)
    rec_coffee_amt = models.IntegerField(blank=True, null=True)

class Preparation(models.Model):

    date = models.DateField('Preparation Date', blank=True)

    grind = models.CharField(max_length=100, blank=True, null=True)
    water_amt = models.IntegerField(blank=True, null=True)
    coffee_amt = models.IntegerField(blank=True, null=True)
    time_amt = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    rating = RatingField(range=5)

    method = models.ForeignKey(Method)
    coffeebag = models.ForeignKey(PurchasedCoffeeBag)
    user = models.ForeignKey(User)

    ## tags for flavor notes?
    # tags = sometaggingappmodel()

    ## Need to investigate how to share b/t users...
