from django.db import models
from django.contrib.auth.models import User
from django import forms

from djangoratings.fields import RatingField

from base.models import Store, CoffeeBag

# Create your models here.

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

class PurchasedCoffeeBagForm(forms.ModelForm):

    formfield_callback = make_custom_datefield
    
    class Meta:
        model = PurchasedCoffeeBag
        exclude = ('user',)
