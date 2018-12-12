from django.contrib import admin
from .models import Room
#from .models import Check_Availability
from .models import UserRegister
from .models import Contact
from .models import Display

#from .models import Cancel

class Roomadmin(admin.ModelAdmin):
    list_display = ['room_type','price','date']
    class meta:
        model=Room

# Register your models here.
admin.site.register(Room,Roomadmin)
#admin.site.register(Check_Availability)
admin.site.register(UserRegister)
admin.site.register(Contact)
#admin.site.register(Cancel)
admin.site.register(Display)