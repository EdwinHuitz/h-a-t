from django.urls import path
from . import views

urlpatterns = [
   path('',views.home,name='home'),
   path('about/',views.about,name='about'),
   path('units/',views.unitIndex,name='unit_index'),
   path('units/{pk:id}',views.unitDetail,name='unit_detail'),
   path('units/add/',views.unitCreate.as_view(),name='unit_create'),
   path('managers/',views.managerIndex,name='manager_index'),
   path('managers/{pk:id}',views.managerDetail,name="manager_detail"),
   path('managers/add/',views.managerCreate,name='manager_create'),
   path('profiles/create/',views.profileCreate,name='profile_create'),
   path('profiles/{pk:id}/',views.profile,name='profile'),
   path('accounts/register/',views.register,name='register'),
]
