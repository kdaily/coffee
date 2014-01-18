import logging

from django import forms
from django.db import models

import selectable.forms

from general.models import Coffee, CoffeeBag, Store, Roaster
from .models import PurchasedCoffeeBag
from .models import Preparation

# Create your views here.

logger = logging.getLogger('views')

def make_custom_datefield(f):
    """Change the format of the date in form fields.
    
    """
    
    formfield = f.formfield()

    if isinstance(f, models.DateField):
        formfield.widget.format = '%Y-%m-%d'
        formfield.widget.attrs.update({'class': 'datePicker', 'readonly': 'true'})

    return formfield

class PreparationForm(forms.ModelForm):

    roaster = forms.ModelChoiceField(queryset=Roaster.objects.all())
    coffeebag = forms.ModelChoiceField(queryset=CoffeeBag.objects.none(), required=False)

    # change the format of the date fields
    formfield_callback = make_custom_datefield
    
    def __init__(self, *args, **kwargs):

        super(PreparationForm, self).__init__(*args, **kwargs)

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

    class Meta:
        model = Preparation

        fields = ('date', 'grinder', 'grind', 'method',
                  'water_amt', 'coffee_amt', 'time_amt',
                  'thumb', 'notes')

        exclude = ('user', 'coffeebag')
