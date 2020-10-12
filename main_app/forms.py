from django.forms import ModelForm
from .models import *

class ammenityForm(ModelForm):
   class Meta:
      model=Amenities
      fields=['name']

class ucommentForm(ModelForm):
   class Meta:
      model=UnitComment
      fields=['title','rating','content']
      
class mcommentForm(ModelForm):
   class Meta:
      model=ManagerComment
      fields=['title','rating','content']
