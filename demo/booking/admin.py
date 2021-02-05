from django.contrib import admin
from .models import Booking, Registertion
# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display =['room_type','from_date','to_date']
admin.site.register(Booking,BookingAdmin)
admin.site.register(Registertion)