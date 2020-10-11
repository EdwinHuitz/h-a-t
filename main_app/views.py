from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView,DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .models import *
from .forms import *

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

def testing(request):
   error_message=''
   if request.method == 'POST':
      form = unitForm(request.POST)
      if form.is_valid():
         return redirect('home')
      else:
         error_message=''
   return render(request,'test/a.html',{'form':form},)

@login_required
def unitDetail(request,unit_id):
   unit=Unit.objects.get(id=unit_id)
   ammenityform=ammenityForm()
   commentform=commentForm()
   return render(request, 'units/details.html',{'unit':unit,'ammenityform':ammenityform,'commentform':commentForm})

@login_required
def addComment(request,unit_id):
   form=commentForm(request.POST)
   if form.is_valid():
      newCom=form.save(commit=False)
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
def memberIndex(request):
   member = Member.objects.all()
   return render(request,'members/index.html',{'members':member})

def register(request):
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

# class unitDetail(LoginRequiredMixin,DetailView):
#    model=Unit
#    template_name='units/details.html'

#! Management
class managerCreate(LoginRequiredMixin,CreateView):
   model=Manager
   fields='__all__'
   template_name='managers/create.html'

class managerView(LoginRequiredMixin,ListView):
   model=Manager
   template_name='managers/index.html'

class managerDetail(LoginRequiredMixin,DetailView):
   model=Manager
   template_name='managers/details.html'

#! Comments
class commentView(LoginRequiredMixin,ListView):
   model=Comment

class commentDelete(LoginRequiredMixin,DeleteView):
   model=Comment

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

class memberEdit(UpdateView):
   model=Member
   fields=['name','bio','email']
   template_name='members/edit.html'
#! Private Lists
class listCreate(CreateView):
   model=PrivateList
   fields=['title']
   template_name='members/list_create.html'