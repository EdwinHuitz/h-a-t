from django.urls import path
from . import views

urlpatterns = [
   path('',views.home,name='home'),
   path('about/',views.about,name='about'),
   path('units/',views.unitIndex,name='unit_index'),
   path('units/<int:pk>/',views.unitDetail.as_view(),name='unit_details'),
   path('units/create/',views.unitCreate.as_view(),name='unit_create'),
   path('managers/',views.managerIndex,name='manager_index'),
   path('managers/<int:pk>/',views.managerDetail.as_view(),name="manager_details"),
   path('managers/create/',views.managerCreate.as_view(),name='manager_create'),
   path('profiles/create/',views.profileCreate,name='profile_create'),
   path('profiles/<int:pk>/',views.profileDetail.as_view(),name='profile_details'),
   path('accounts/register/',views.register,name='register'),
]
