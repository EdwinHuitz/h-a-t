from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

RATINGS=(
   (1,1),
   (2,2),
   (3,3),
   (4,4),
   (5,5),
)
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
# Create your models here. 
class Member(models.Model):
   name= models.CharField(max_length=100)
   bio=  models.TextField(blank=True)
   email=models.EmailField(max_length=100)
   user= models.ForeignKey(User,on_delete=models.CASCADE)
   def __str__(self):
      return self.name
   def get_absolute_url(self):
      return reverse('member_details',kwargs={'pk':self.id})

class PrivateList(models.Model):
   title=   models.CharField(max_length=100)
   profile= models.ForeignKey(Member,on_delete=models.CASCADE)
   def __str__(self):
      return self.title
   def get_absolute_url(self):
      return reverse('list_details',kwargs={'pl':self.id})

class Manager(models.Model):
   name=    models.CharField(max_length=100)
   address= models.CharField(max_length=100)
   contact= models.CharField(max_length=100)
   def __str__(self):
      return self.name
   def get_absolute_url(self):
      return reverse('manager_details',kwargs={'mg_id':self.id})

class Unit(models.Model):
   name=       models.CharField(max_length=100)
   address=    models.CharField(max_length=100)
   manager=    models.ForeignKey(Manager,on_delete=models.DO_NOTHING)
   privatelist=models.ManyToManyField('PrivateList')
   contact=    models.CharField(max_length=100)
   def __str__(self):
      return self.name
   def get_absolute_url(self):
      return reverse('unit_details',kwargs={'unit_id':self.id})

class Amenities(models.Model):
   name=models.CharField(
      max_length=2,
      choices=AMENITIES,
      default=AMENITIES[0][0]
   )
   unit=models.ForeignKey(Unit,on_delete=models.CASCADE)

   def __str__(self):
      return f"{self.get_name_display()}"

class UnitComment(models.Model):
   title=   models.CharField(max_length=100)
   rating=  models.SmallIntegerField(
      choices=RATINGS,
      default=RATINGS[0][0]
   )
   date=       models.DateField(auto_now_add=True)
   content=    models.TextField()
   user=       models.ForeignKey(User,on_delete=models.CASCADE)
   unit=       models.ForeignKey(Unit,on_delete=models.CASCADE)
   def __str__(self):
      return self.title
   class Meta:
    ordering = ['-date']
   def get_absolute_url(self):
      return reverse('comment_udetails',kwargs={'pk':self.id})

class ManagerComment(models.Model):
   title=   models.CharField(max_length=100)
   rating=  models.SmallIntegerField(
      choices=RATINGS,
      default=RATINGS[0][0]
   )
   date=       models.DateField(auto_now_add=True)
   content=    models.TextField()
   user=       models.ForeignKey(User,on_delete=models.CASCADE)
   manager=    models.ForeignKey(Manager,on_delete=models.CASCADE)
   def __str__(self):
      return self.title
   class Meta:
    ordering = ['-date']
   def get_absolute_url(self):
      return reverse('comment_mdetails',kwargs={'pk':self.id})

class ListComment(models.Model):
   title=   models.CharField(max_length=100)
   rating=  models.SmallIntegerField(
      choices=RATINGS,
      default=RATINGS[0][0]
   )
   date=       models.DateField(auto_now_add=True)
   content=    models.TextField()
   user=       models.ForeignKey(User,on_delete=models.CASCADE)
   privatelist=models.ForeignKey(PrivateList,on_delete=models.CASCADE)
   def __str__(self):
      return self.title
   class Meta:
    ordering = ['-date']
   def get_absolute_url(self):
      return reverse('comment_ldetails',kwargs={'pk':self.id})

class UnitPhoto(models.Model):
   url = models.CharField(max_length=200)
   unit = models.ForeignKey(Unit,on_delete=models.CASCADE)
   def __str__(self):
      return f"unit photo for {self.unit_id}@{self.url}"

class ManagerPhoto(models.Model):
   url = models.CharField(max_length=200)
   manager = models.ForeignKey(Manager,on_delete=models.CASCADE)
   def __str__(self):
      return f"unit photo for {self.manager_id}"

class ProfilePhoto(models.Model):
   url = models.CharField(max_length=200)
   member = models.ForeignKey(Member,on_delete=models.CASCADE)
   def __str__(self):
      return f"member photo for {self.member_id}"