from django.urls import path
from . import views

urlpatterns = [
   #! Public
   path('',views.home,name='home'),
   path('about/',views.about,name='about'),
   #! Units
   path('units/',views.unitIndex,name='unit_index'),
   path('units/<int:unit_id>/',views.unitDetail,name='unit_details'),
   path('units/create/',views.unitCreate.as_view(),name='unit_create'),
   path('units/<int:unit_id>/amenity/',views.addAmenity,name='add_amenity'),
   path('units/<int:unit_id>/add_comment/',views.addUnitComment,name='add_ucomment'),
   path('units/<int:unit_id>/comments/<int:pk>/delete/',views.UcommentDelete.as_view(),name='delete_ucomment'),
   path('units/<int:unit_id>/add_photo/',views.addUnitPhoto,name='add_uphoto'),
   #! Managers
   path('managers/',views.managerIndex,name='manager_index'),
   path('managers/<int:mg_id>/',views.managerDetail,name='manager_details'),
   path('managers/<int:mg_id>/add_comment/',views.addManagerComment,name='add_mcomment'),
   path('managers/<int:mg_id>/comments/<int:pk>/delete/',views.McommentDelete.as_view(),name='delete_mcomment'),
   path('managers/create/',views.managerCreate.as_view(),name='manager_create'),
   path('managers/<int:mg_id>/add_photo/',views.addManagerPhoto,name='add_mphoto'),
   #! Members
   path('members/<int:pk>/',views.memberDetail.as_view(),name='member_details'),
   path('members/create/',views.memberCreate.as_view(),name='member_create'),
   path('members/<int:pk>/edit/',views.memberEdit.as_view(),name='member_edit'),
   path('members/<int:pk>/photo/',views.addMemberPhoto,name='add_memphoto'),
   #! Other
   path('members/list/create/',views.listCreate.as_view(),name='list_create'),
   path('accounts/register/',views.register,name='register'),
]
