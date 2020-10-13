from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView,DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
import uuid
import boto3
from .models import *
from .forms import *
S3_BASE_URL='https://s3.us-east-1.amazonaws.com/'
BUCKET='catterday'
# view functions
def home(request):
   unit = Unit.objects.all()
   return render(request,'home.html',{'units':unit})

def about(request):
   return render(request,'about.html')

@login_required
def unitIndex(request):
   unit = Unit.objects.all()
   return render(request,'units/index.html',{'units':unit})

@login_required
def unitDetail(request,unit_id):
   unit=Unit.objects.get(id=unit_id)
   ammenityform=ammenityForm()
   commentform=ucommentForm()
   return render(request, 'units/details.html',{'unit':unit,'ammenityform':ammenityform,'commentform':commentform})

@login_required
def addUnitComment(request,unit_id):
   form=ucommentForm(request.POST)
   if form.is_valid():
      newCom=form.save(commit=False)
      newCom.user_id=request.user.id
      newCom.unit_id=unit_id
      newCom.save()
   return redirect('unit_details',unit_id=unit_id)

@login_required
def addAmenity(request,unit_id):
   form=ammenityForm(request.POST)
   if form.is_valid():
      newAm=form.save(commit=False)
      newAm.unit_id=unit_id
      newAm.save()
   return redirect('unit_details',unit_id=unit_id)

@login_required
def managerIndex(request):
   manager = Manager.objects.all()
   return render(request,'managers/index.html',{'managers':manager})

@login_required
def managerDetail(request,mg_id):
   manager=Manager.objects.get(id=mg_id)
   commentform=mcommentForm()
   return render(request, 'managers/details.html',{'manager':manager,'commentform':commentform})

@login_required
def addManagerComment(request,mg_id):
   form=mcommentForm(request.POST)
   if form.is_valid():
      newCom=form.save(commit=False)
      newCom.user_id=request.user.id
      newCom.manager_id=mg_id
      newCom.save()
   return redirect('manager_details',mg_id=mg_id)

@login_required
def memberIndex(request):
   member = Member.objects.all()
   return render(request,'members/index.html',{'members':member})

@login_required
def addUnitPhoto(request,unit_id):
   unitpic = request.FILES.get('photo-file',None)
   if unitpic:
      s3=boto3.client('s3')
      key=uuid.uuid4().hex[:6]+unitpic.name[unitpic.name.rfind('.'):]
      try:
         s3.upload_fileobj(unitpic,BUCKET,key)
         url=f"{S3_BASE_URL}{BUCKET}/{key}"
         photo = UnitPhoto(url=url,unit_id=unit_id)
         photo.save()
      except:
         print('An error occured uploading your photo')
   return redirect('unit_details',unit_id=unit_id)

@login_required
def addManagerPhoto(request,mg_id):
   mgpic = request.FILES.get('photo-file',None)
   if mgpic:
      s3=boto3.client('s3')
      key=uuid.uuid4().hex[:6]+mgpic.name[mgpic.name.rfind('.'):]
      try:
         s3.upload_fileobj(mgpic,BUCKET,key)
         url=f"{S3_BASE_URL}{BUCKET}/{key}"
         photo = ManagerPhoto(url=url,manager_id=mg_id)
         photo.save()
      except:
         print('An error occured uploading your photo')
   return redirect('manager_details',mg_id=mg_id)

@login_required
def addMemberPhoto(request,member):
   memberpic = request.FILES.get('photo-file',None)
   if memberpic:
      s3=boto3.client('s3')
      key=uuid.uuid4().hex[:6]+memberpic.name[memberpic.name.rfind('.'):]
      try:
         s3.upload_fileobj(memberpic,BUCKET,key)
         url=f"{S3_BASE_URL}{BUCKET}/{key}"
         photo = Member(url=url,member_id=member)
         photo.save()
      except:
         print('An error occured uploading your photo')
   return redirect('member_details',pk=member)
   
# def listCreate(request,list_id):
#    form=listForm(request.POST)
#    if form.is_valid():
#       newList=form.save(commit=False)
#       newList.user_id=request.user.id
#       newList.save()
#    return redirect('list_details',pl=list_id)

def register(request):
   form=registerForm(request.POST)
   if form.is_valid():
      newCom=form.save(commit=False)
      newCom.user_id=request.user.id
      newCom.manager_id=mg_id
      newCom.save()
   return redirect('manager_details',mg_id=mg_id)

   error_message=''
   if request.method == 'POST':
      form=UserCreationForm(request.POST)
      if form.is_valid():
         user=form.save()
         login(request,user)
         return redirect('member_create')
      else:
         error_message='Invalid Registration: Try Again'
   form=UserCreationForm()
   context={'form':form,'error_message':error_message}
   return render(request,'registration/register.html',context)



# classes
#! Units

class unitCreate(LoginRequiredMixin,CreateView):
   model=Unit
   fields=['name','address','contact','manager']
   template_name='units/create.html'

class unitView(LoginRequiredMixin,ListView):
   model=Unit
   template_name='units/index.html'

#! Management
class managerCreate(LoginRequiredMixin,CreateView):
   model=Manager
   fields='__all__'
   template_name='managers/create.html'

class managerView(LoginRequiredMixin,ListView):
   model=Manager
   template_name='managers/index.html'

#! Comments
class UcommentView(LoginRequiredMixin,ListView):
   model=UnitComment

class UcommentDelete(LoginRequiredMixin,DeleteView):
   model=UnitComment
   success_url='/units/'
class McommentView(LoginRequiredMixin,ListView):
   model=ManagerComment

class McommentDelete(LoginRequiredMixin,DeleteView):
   model=ManagerComment
   success_url='/managers/'

#! Profiles
class memberCreate(CreateView):
   model=Member
   fields=['name','bio','email']
   template_name='members/create.html'
   def form_valid(self,form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class memberDetail(LoginRequiredMixin,DetailView):
   model=Member
   template_name='members/details.html'

class memberEdit(LoginRequiredMixin,UpdateView):
   model=Member
   fields=['name','bio','email']
   template_name='members/edit.html'

# class listDetail(LoginRequiredMixin,DetailView):
#    model=PrivateList
#    template_name='members/list_view.html'