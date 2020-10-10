from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView,DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *


# view functions
def home(request):
   return render(request,'home.html')

def about(request):
   return render(request,'about.html')

def unitIndex(request):
   unit = Unit.objects.all()
   return render(request,'units/index.html',{'units':unit})

def managerIndex(request):
   manager = Manager.objects.all()
   return render(request,'managers/index.html',{'managers':manager})

def memberIndex(request):
   member = Member.objects.all()
   return render(request,'members/details.html',{'members':member})

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
class unitCreate(CreateView):
   model=Unit
   fields=['name','address','contact','manager']
   template_name='units/create.html'

class unitView(ListView):
   model=Unit
   template_name='units/index.html'

class unitDetail(DetailView):
   model=Unit
   template_name='units/details.html'

#! Management
class managerCreate(CreateView):
   model=Manager
   fields='__all__'
   template_name='managers/create.html'

class managerView(ListView):
   model=Manager
   template_name='managers/index.html'

class managerDetail(DetailView):
   model=Manager
   template_name='managers/details.html'

#! Comments
class commentView(ListView):
   model=Comment

class commentDelete(DeleteView):
   model=Comment

#! Profiles
class memberCreate(CreateView):
   model=Member
   fields="__all__"
   template_name='members/create.html'
   def form_valid(self,form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class memberDetail(DetailView):
   model=Member
   template_name='members/details.html'