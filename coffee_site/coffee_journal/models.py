from django.db import models
from django.contrib.auth.models import User
from django import forms

from djangoratings.fields import RatingField

from base.models import Store, CoffeeBag

class PurchasedCoffeeBag(models.Model):
    """DB model for a purchased coffee bag.
    
    Has relationships to a user, store, and coffee bag.
    
    """
    
    date_purch = models.DateField('Purchase Date', blank=True)
    rating = RatingField(range=5)

    notes = models.TextField(blank=True, null=True)

    user = models.ManyToManyField(User)
    store = models.ForeignKey(Store)
    coffeebag = models.ForeignKey(CoffeeBag)

    def __unicode__(self):
        return "%s, %s, %s" % (self.coffeebag.coffee.name, self.coffeebag.roaster.name, self.store.name)

    class Meta:
        # Default ordering - chronological by purchase date
        ordering = ["-date_purch"]


def make_custom_datefield(f):
    """Change format of date fields in form.
    
    Should move to a utilities module.
    
    """
    
    formfield = f.formfield()
    if isinstance(f, models.DateField):
        formfield.widget.format = '%Y-%m-%d'
        formfield.widget.attrs.update({'class': 'datePicker', 'readonly': 'true'})
    return formfield

class PurchasedCoffeeBagForm(forms.ModelForm):
    """Form model for purchased coffee bags.
    
    """

    # Change format of date fields in form.
    formfield_callback = make_custom_datefield
    
    class Meta:
        model = PurchasedCoffeeBag
        
        # Logged in user will add a purchased coffee bag
        # so in form the user field should not be displayed.
        exclude = ('user',)
