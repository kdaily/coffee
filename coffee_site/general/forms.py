from django import forms
from django.db import models

import selectable.forms

from .models import Coffee, CoffeeBag, Store, Roaster
from .lookups import RoasterLookup

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

    autocomplete = forms.CharField(label='Roaster',
                                   widget=selectable.forms.AutoCompleteWidget(RoasterLookup),
                                   required=False)
    
    class Meta:
        model = CoffeeBag
        
        exclude = ('thumb',)

class StoreForm(forms.ModelForm):
    """Form model for adding new stores.
    
    """
        
    class Meta:
        model = Store

class RoasterForm(forms.ModelForm):
    """Form model for adding new stores.
    
    """

    autocomplete = forms.CharField(
        label='Type the name of a roaster',
        widget=selectable.forms.AutoCompleteWidget(RoasterLookup),
        required=False,
    )    

    
    class Meta:
        model = Roaster

        fields = ('autocomplete', 'address', 'city', 'state', 'zipcode', 'website', 
                  'phone', 'fbook', 'twitter', 'gplus')
        exclude = ('lgt', 'lat',)

class RoasterLookupForm(forms.Form):

    roaster = forms.ModelChoiceField(queryset=Roaster.objects.all())
    coffeebag = forms.ModelChoiceField(queryset=CoffeeBag.objects.none(), required=False)
    
    def __init__(self, *args, **kwargs):

        super(RoasterLookupForm, self).__init__(*args, **kwargs)
        forms.Form.__init__(self, *args, **kwargs)

        roasters = Roaster.objects.all()

        if len(roasters) == 1:
            self.fields['roaster'].initial = roasters[0].pk

        roaster_id = self.fields['roaster'].initial or \
            self.initial.get('roaster') or \
            self._raw_value('roaster')
        
        if roaster_id:
            # roaster is known. Now I can display the matching coffee bags.
            coffeebags = CoffeeBag.objects.filter(roaster__id=roaster_id)
            self.fields['coffeebag'].queryset = coffeebags

            if len(coffeebags) == 1:
                self.fields['coffeebag'].initial = coffeebags[0].pk
