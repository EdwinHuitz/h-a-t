from django.contrib import admin
from .models import *
# Register your models here.
a=admin.site
a.register(Member)
a.register(Unit)
a.register(UnitComment)
a.register(Amenities)
a.register(Manager)
a.register(ManagerComment)
a.register(PrivateList)
a.register(ListComment)
a.register(UnitPhoto)