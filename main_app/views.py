from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView,DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

# Create your views here.
def home(request):
   return render(request,'home.html')

def about(request):
   return render(request,'about.html')

def unitIndex(request):
   unit = Unit.objects.all()
   return render(request,'units/index.html',{'unit':unit})


def managementIndex(request):
   management = Management.objects.all()
   return render(request,'management/index.html',{'management':management})


def profile(request):
   profile = Profile.objects.all()
   return render(request,'profiles/details.html',{'profile':profile})

def register(request):
   error_message=''
   if request.method == 'POST':
      form=UserCreationForm(request.POST)
      if form.is_valid():
         user=form.save()
         login(request,user)
         return redirect('index')
      else:
         error_message='Invalid Registration: Try Again'
   form=UserCreationForm()
   context={'form':form,'error_message':error_message}
   return render(request,'registration/register.html',context)

class profileCreate(CreateView):
   model=Profile
   fields="__all__"
   def form_valid(self,form):
      form.instance.user = self.request.user
      return super().form_valid(form)
