from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

RATINGS=(
   ('-5',-5),
   ('-4',-4),
   ('-3',-3),
   ('-2',-2),
   ('-1',-1),
   ('0',0),
   ('1',1),
   ('2',2,),
   ('3',3),
   ('4',4),
   ('5',5)
)
# Create your models here. 
class Member(models.Model):
   name= models.CharField(max_length=100)
   bio=  models.TextField(blank=True)
   email=models.EmailField(max_length=100)
   user= models.ForeignKey(User,on_delete=models.CASCADE)
   def __string__(self):
      return self.name
   def get_absolute_url(self):
      return reverse('member_details',kwargs={'pk':self.id})

class PrivateList(models.Model):
   title=   models.CharField(max_length=100)
   profile= models.ForeignKey(Member,on_delete=models.CASCADE)
   def __string__(self):
      return self.name
   def get_absolute_url(self):
      return reverse('list_details',kwargs={'pl':self.id})

class Manager(models.Model):
   name=    models.CharField(max_length=100)
   address= models.CharField(max_length=100)
   contact= models.CharField(max_length=100)
   def __string__(self):
      return self.name
   def get_absolute_url(self):
      return reverse('manager_details',kwargs={'pk':self.id})

class Unit(models.Model):
   name=       models.CharField(max_length=100)
   address=    models.CharField(max_length=100)
   manager=    models.ForeignKey(Manager,on_delete=models.CASCADE,)
   privatelist=models.ManyToManyField('PrivateList')
   contact=    models.CharField(max_length=100)
   def __string__(self):
      return self.name
   def get_absolute_url(self):
      return reverse('unit_details',kwargs={'pk':self.id})

class Comment(models.Model):
   title=   models.CharField(max_length=100)
   rating=  models.SmallIntegerField(
      choices=RATINGS,
      default=RATINGS[0][0]
   )
   date=       models.DateField(auto_now_add=True)
   content=    models.TextField()
   user=       models.ForeignKey(Member,on_delete=models.CASCADE)
   manager=    models.ForeignKey(Manager,on_delete=models.CASCADE,)
   unit=       models.ForeignKey(Unit,on_delete=models.CASCADE,)
   privatelist=models.ForeignKey(PrivateList,on_delete=models.CASCADE,)
   def __string__(self):
      return self.name
   def get_absolute_url(self):
      return reverse('comment_details',kwargs={'cm':self.id})
