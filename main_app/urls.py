from django.urls import path
from . import views

urlpatterns = [
   path('',views.home,name='home'),
   path('about/',views.about,name='about'),
   path('units/',views.unitIndex,name='unit_index'),
   path('units/<int:unit_id>/',views.unitDetail,name='unit_details'),
   path('units/create/',views.unitCreate.as_view(),name='unit_create'),
   path('units/<int:unit_id>/amenity/',views.addAmenity,name='add_amenity'),
   path('units/<int:unit_id>/comment/',views.addComment,name='add_comment'),
   path('test/',views.testing,name="test"),
   path('managers/',views.managerIndex,name='manager_index'),
   path('managers/<int:pk>/',views.managerDetail.as_view(),name='manager_details'),
   path('managers/create/',views.managerCreate.as_view(),name='manager_create'),
   path('members/<int:pk>/',views.memberDetail.as_view(),name='member_details'),
   path('members/create/',views.memberCreate.as_view(),name='member_create'),
   path('members/<int:pk>/edit/',views.memberEdit.as_view(),name='member_edit'),
   path('members/list/create/',views.listCreate.as_view(),name='list_create'),
   path('accounts/register/',views.register,name='register'),
]
