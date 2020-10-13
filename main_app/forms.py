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

class registerForm(ModelForm):
   class Meta:
      model=User
      fields=['username','password']

# class listForm(ModelForm):
#    class Meta:
#       model=PrivateList
#       fields='__all__'