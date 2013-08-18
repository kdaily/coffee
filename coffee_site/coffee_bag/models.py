from django.db import models
from django.contrib.auth.models import User
from django import forms

from sorl.thumbnail import ImageField

from djangoratings.fields import RatingField

from general.models import UserStore, CoffeeBag

class PurchasedCoffeeBag(models.Model):
    """DB model for a purchased coffee bag.
    
    Has relationships to a user, store, and coffee bag.
    
    """
    
    date_purch = models.DateField('Purchase Date', blank=True)
    rating = RatingField(range=5)

    notes = models.TextField(blank=True, null=True)    

    thumb = ImageField(upload_to='/media/img/', blank=True)

    user = models.ManyToManyField(User)
    store = models.ForeignKey(UserStore)
    coffeebag = models.ForeignKey(CoffeeBag)
    
    #This needs to be replaced with something else, once we set up the groups
    is_shared = models.IntegerField()

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
