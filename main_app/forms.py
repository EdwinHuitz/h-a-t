from django.forms import ModelForm
from .models import *

class ammenityForm(ModelForm):
   class Meta:
      model=Amenities
      fields=['name']

class commentForm(ModelForm):
   class Meta:
      model=Comment
      fields=['title','rating','content']