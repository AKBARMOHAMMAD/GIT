from django.contrib import admin
from .models import Room
from .models import Review
from .models import Check_Availability
from .models import UserRegister
from .models import ContactUs

# Register your models here.
admin.site.register(Room)
admin.site.register(Review)
admin.site.register(Check_Availability)
admin.site.register(UserRegister)
admin.site.register(ContactUs)
