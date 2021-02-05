from django.contrib import admin
from .models import Room,RoomType 
# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    list_display =['room_no','bedtype','roomtype']

admin.site.register(Room,RoomAdmin)
admin.site.register(RoomType)