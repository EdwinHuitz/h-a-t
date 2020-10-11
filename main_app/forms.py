from django.forms import ModelForm
from .models import *

class listForm(ModelForm):
   class Meta:
      model=Amenities
      fields=['name']