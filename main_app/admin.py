from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Member)
admin.site.register(Unit)
admin.site.register(UnitComment)
admin.site.register(Amenities)
admin.site.register(Manager)
admin.site.register(ManagerComment)
admin.site.register(PrivateList)
admin.site.register(ListComment)