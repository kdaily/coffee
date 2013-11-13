from django.db import models
from django import forms
from django.conf import settings

from sorl.thumbnail import ImageField

from djangoratings.fields import RatingField

from general.models import Store, CoffeeBag, CoffeeBagImage

    
class PurchasedCoffeeBag(models.Model):
    """DB model for a purchased coffee bag.
    
    Has relationships to a user, store, and coffee bag.
    
    """
    
    date_purch = models.DateField('Purchase Date', blank=True)
        
    rating = RatingField(range=5, weight=5, can_change_vote=True, allow_delete=True, allow_anonymous=False)

    notes = models.TextField(blank=True, null=True)    

    thumb = models.ForeignKey(CoffeeBagImage, blank=True, null=True)

    # Better way to specify the user than the User object
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)
    store = models.ForeignKey(Store, blank=False, null=False)
    coffeebag = models.ForeignKey(CoffeeBag, blank=False, null=False)
    
    def __unicode__(self):
        return "%s, %s, %s" % (self.coffee_bag.coffee.name, 
                               self.coffee_bag.roaster.name,
                               self.store.name)

    class Meta:
        # Default ordering - chronological by purchase date
        ordering = ["-date_purch"]

        permissions = (('view_purch_coffee_bag', 'View purchased coffee bag'),)

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
        exclude = ('user', 'coffeebag')
