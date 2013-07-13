from django.db import models
from django.contrib.auth.models import User
from django import forms

from djangoratings.fields import RatingField
from sorl.thumbnail import ImageField

class Roaster(models.Model):
    name = models.CharField(max_length=500)
    city = models.CharField(max_length=500, blank=True, null=True)
    state = models.CharField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    zipcode = models.IntegerField(blank=True, null=True)
    website = models.CharField(max_length=500, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return "%s" % (self.name)

class Store(models.Model):
    name = models.CharField(max_length=500)
    city = models.CharField(max_length=500, blank=True, null=True)
    state = models.CharField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    zipcode = models.IntegerField(blank=True, null=True)
    website = models.CharField(max_length=500, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return "%s" % (self.name)

# Create your models here.
class Coffee(models.Model):
    """DB model for coffee.

    """
    
    # required fields
    name = models.CharField(max_length=500)

    grower = models.CharField(max_length=500, blank=True, null=True)
    finca = models.CharField(max_length=500, blank=True, null=True)
    varietal = models.CharField(max_length=200, blank=True, null=True)

    country = models.CharField(max_length=3, blank=True, null=True)

    altitude = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)


    def __unicode__(self):
        return "%s" % (self.name)

class CoffeeBag(models.Model):

    date_roast = models.DateField('Roast Date', blank=True, null=True)
    
    amount = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    thumb = ImageField(upload_to='/media/img/', blank=True)

    roaster = models.ForeignKey(Roaster)
    store = models.ForeignKey(Store)
    coffee = models.ForeignKey(Coffee)

    def __unicode__(self):
        return "%s, %s, %s" % (self.coffee.name, self.roaster.name, self.store.name)


class PurchasedCoffeeBag(models.Model):

    # purch_location = models.CharField(max_length=500)
    date_purch = models.DateField('Purchase Date', blank=True)

    rating = RatingField(range=5)

    user = models.ManyToManyField(User)
    store = models.ForeignKey(Store)
    coffeebag = models.ForeignKey(CoffeeBag)

    def __unicode__(self):
        return "%s, %s, %s" % (self.coffeebag.coffee.name, self.coffeebag.roaster.name, self.coffeebag.store.name)


def make_custom_datefield(f):
    formfield = f.formfield()
    if isinstance(f, models.DateField):
        formfield.widget.format = '%Y-%m-%d'
        formfield.widget.attrs.update({'class': 'datePicker', 'readonly': 'true'})
    return formfield


class CoffeeForm(forms.ModelForm):

    formfield_callback = make_custom_datefield
    
    class Meta:
        model = Coffee
        exclude = ('user',)

class CoffeeBagForm(forms.ModelForm):

    formfield_callback = make_custom_datefield
    
    class Meta:
        model = CoffeeBag
        exclude = ('user',)


class PurchasedCoffeeBagForm(forms.ModelForm):

    formfield_callback = make_custom_datefield
    
    class Meta:
        model = PurchasedCoffeeBag
        exclude = ('user',)


    # widgets = {
    #     'date_purch': forms.DateInput(format='%Y-%m-%d', attrs={'class':'datePicker', 'readonly':'true'}),
    #     'date_roast': forms.DateInput(format='%Y-%m-%d', attrs={'class':'datePicker', 'readonly':'true'}),
    #     }

