from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Fabric, Fvendor, Inventory, F_V, Saleprice

admin.site.register(Fabric)
admin.site.register(Fvendor)
admin.site.register(Inventory)
admin.site.register(F_V)
admin.site.register(Saleprice)

##password: Abhi
#user: abhishekpandey 