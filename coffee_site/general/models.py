from django.db import models
from django import forms

from sorl.thumbnail import ImageField

class Roaster(models.Model):
    """Model for a roaster.
    
    """
    
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=500, blank=True, null=True)
    state = models.CharField(max_length=500, blank=True, null=True)
    zipcode = models.IntegerField(null=True)
    country = models.CharField(max_length=3, null=True)
    
    website = models.CharField(max_length=500, blank=True, null=True)
    phone = models.IntegerField(null=True)

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


    def __unicode__(self):
        return "%s (%s)" % (self.name, self.finca)

    class Meta:
        # the columns that make unique records
        unique_together = ("name", "grower", "finca")
    
class CoffeeBag(models.Model):
    """DB model for a coffee bag.

    This has a roaster and a coffee as relationships.

    """

    date_roast = models.DateField('Roast Date', blank=True, null=True)
    
    amount = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    thumb = ImageField(upload_to='/media/img/', blank=True)

    roaster = models.ForeignKey(Roaster)
    coffee = models.ForeignKey(Coffee)

    def __unicode__(self):
        return "%s, %s (%s)" % (self.coffee.name, self.roaster.name, self.date_roast)

    class Meta:
        # the columns that make unique records
        unique_together = ('roaster', 'coffee', 'date_roast')
        
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
