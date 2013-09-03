from django.db import models
from django import forms
from django.conf import settings

from sorl.thumbnail import ImageField
from djangoratings.fields import RatingField

class Roaster(models.Model):
    """Model for a roaster.
    
    """
    
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=500, blank=True, null=True)
    state = models.CharField(max_length=500, blank=True, null=True)
    zipcode = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=3, null=True, blank=True)
    
    website = models.CharField(max_length=500, blank=True, null=True)
    phone = models.IntegerField(null=True, blank=True)
    
    fbook  = models.CharField(max_length=500, blank=True, null=True)
    twitter  = models.CharField(max_length=500, blank=True, null=True)
    gplus  = models.CharField(max_length=500, blank=True, null=True)
     
    #To use ImageFields, you need to install the Python Imaging Library
    thumb = models.ImageField(upload_to='/media/img/', blank=True)
    
    rating = RatingField(range=5)

    def __unicode__(self):
        return "%s" % (self.name)

    class Meta:
        # the columns that make unique records
        unique_together = ('name', 'city', 'state')

class Store(models.Model):
    """Model for a store.
    
    """
    
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=500, blank=True, null=True)
    state = models.CharField(max_length=500, blank=True, null=True)
    zipcode = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=3, blank=True, null=True)
    website = models.CharField(max_length=500, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)

    fbook  = models.CharField(max_length=500, blank=True, null=True)
    twitter  = models.CharField(max_length=500, blank=True, null=True)
    gplus  = models.CharField(max_length=500, blank=True, null=True)
    
    #To use ImageFields, you need to install the Python Imaging Library
    thumb = models.ImageField(upload_to='/media/img/', blank=True)
    
    rating = RatingField(range=5)
    
    def __unicode__(self):
        return "%s (%s, %s)" % (self.name, self.city, self.state)

# Create your models here.
class Coffee(models.Model):
    """DB model for coffee.

    """
    
    # required fields
    name = models.CharField(max_length=500)

    grower = models.CharField(max_length=500, blank=True, null=True)
    finca = models.CharField(max_length=500, blank=True, null=True)
    region = models.CharField(max_length=500, blank=True, null=True)
    country = models.CharField(max_length=3, blank=True, null=True)
    
    varietal = models.CharField(max_length=200, blank=True, null=True)
    altitude = models.IntegerField(blank=True, null=True)    
    
    notes = models.TextField(blank=True, null=True)
       
    rating = RatingField(range=5)

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.finca)

    class Meta:
        # the columns that make unique records
        unique_together = ("name", "grower", "finca")
    
class RoastedCoffeeBag(models.Model):
    """DB model for a bag of roasted coffee.

    This has a roaster and a coffee as relationships.

    """
    roast_type = models.CharField(max_length=200, blank=True, null=True)

    #To use ImageFields, you need to install the Python Imaging Library
    thumb = models.ImageField(upload_to='/media/img/', blank=True)

    roaster = models.ForeignKey(Roaster)
    coffee = models.ForeignKey(Coffee)

    rating = RatingField(range=5)
    
    def __unicode__(self):
        return "%s, %s (%s)" % (self.coffee.name, self.roaster.name)

    class Meta:
        # the columns that make unique records
        unique_together = ('roaster', 'coffee')
    
class CoffeeBag(models.Model):
    """DB model for a specific coffee bag.

    """
    
    #Maybe we should only have a year?
    date_roast = models.DateField('Roast Date', blank=True, null=True)
    
    amount = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    
    #To use ImageFields, you need to install the Python Imaging Library
    thumb = models.ImageField(upload_to='/media/img/', blank=True)

    roasted_coffee_bag = models.ForeignKey(RoastedCoffeeBag)

    rating = RatingField(range=5)
    
    def __unicode__(self):
        return "%s, %s (%s)" % (self.roasted_coffee_bag.coffee, self.roasted_coffee_bag.roaster, self.date_roast)

    class Meta:
        # the columns that make unique records
        unique_together = ('roasted_coffee_bag', 'date_roast')
        
class AromaTaste(models.Model):
    """Model for a aroma/taste wheel
    
    """
    
    type = models.IntegerField(null=True)
    name = models.CharField(max_length=500)
    parent = models.CharField(max_length=500)

    def __unicode__(self):
        return "%s" % (self.name)
    
class UserRoaster(models.Model):
    """DB model for a user's roasters.
    
    Has relationships to a user and roaster
    """
    
    rating = RatingField(range=5)

    notes = models.TextField(blank=True, null=True)    

    user = models.ManyToManyField(settings.AUTH_USER_MODEL)
    roaster = models.ForeignKey(Roaster)
    

    class Meta:
        permissions = (('view_user_coffee_roaster', "View user's roaster"),)


class UserStore(models.Model):
    """DB model for a user's stores.
    
    Has relationships to a user and store
    """
    
    rating = RatingField(range=5)

    notes = models.TextField(blank=True, null=True)    

    user = models.ManyToManyField(settings.AUTH_USER_MODEL)
    store = models.ForeignKey(Store)

    class Meta:
        permissions = (('view_user_store', "View user's stores"),)

class RoasterStore(models.Model):
    """DB model for a user's roasters.
    
    Has relationships to a user and roaster
    """
    
    rating = RatingField(range=5)
    notes = models.TextField(blank=True, null=True)    

    store = models.ManyToManyField(Store)
    roaster = models.ForeignKey(Roaster)
    roasted_coffee_bag = models.ForeignKey(RoastedCoffeeBag)
    
class NewsInfo(models.Model):
    """news for the first page.
    
    """
    date_post = models.DateField('Date', blank=True)
    title = models.CharField(max_length=500)
    text = models.TextField(blank=True, null=True)   
    source = models.CharField(max_length=500, blank=True, null=True)
    website = models.CharField(max_length=500, blank=True, null=True)
    thumb = models.ImageField(upload_to='/media/img/', blank=True)
    posted_by = models.ManyToManyField(settings.AUTH_USER_MODEL)
    
    
            
def make_custom_datefield(f):
    """Change the format of the date in form fields.
    
    """
    
    formfield = f.formfield()

    if isinstance(f, models.DateField):
        formfield.widget.format = '%Y-%m-%d'
        formfield.widget.attrs.update({'class': 'datePicker', 'readonly': 'true'})

    return formfield

class CoffeeForm(forms.ModelForm):
    """Form model for adding new coffees.
    
    """
    
    # change the format of the date fields
    formfield_callback = make_custom_datefield
    
    class Meta:
        model = Coffee
        
class CoffeeBagForm(forms.ModelForm):
    """Form model for adding new coffees.
    
    """
    
    # change the format of the date fields
    formfield_callback = make_custom_datefield
    
    class Meta:
        model = CoffeeBag
    
