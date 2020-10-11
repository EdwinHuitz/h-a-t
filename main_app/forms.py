from django import forms
from django.forms import ModelForm
from .models import *
AMENITIES=(
   ('ac','Air Conditioning'),
   ('ch','Central Heating'),
   ('ra','Rustic Heating(Radiator)'),
   ('wd','In Unit Washer/Dryer'),
   ('lf','Laundry Facilities'),
   ('p','Parking'),
   ('fw','Free Wifi'),
   ('fc','Free Cable'),
   ('sp','Swimming Pool'),
   ('fc','Fitness Center'),
   ('cd','Cat/Dog Friendly'),
   ('ui','Utilities Included'),
   ('m','Free Pets(Mice Infestation)'),
   ('r',"Free Pest Control(Roach Infestation)"),
)

class unitForm(forms.Form):
   class Meta:
      name=forms.CharField()
      address=forms.CharField()
      contact=forms.CharField()
      amenities=forms.CharField(widget=forms.CheckboxSelectMultiple(choices=AMENITIES))