from django.urls import path
from . import views

urlpatterns = [
   path('',views.home,name='home'),
   path('about/',views.about,name='about'),
   path('units/',views.unitIndex,name='index'),
   path('management/',views.managementIndex,name='management_index'),
   path('profiles/{pk:id}/',views.profile,name='profile'),
   path('accounts/register/',views.register,name='register'),
]
