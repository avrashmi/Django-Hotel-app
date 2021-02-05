import uuid
from django.db import models


# Create your models here.
class RoomType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Room(models.Model):
    bed_type =[
        ('1','single'),
        ('2','double'),
        ('3','triple'),
    ]
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    room_no =models.IntegerField()
    roomtype = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    room_active = models.BooleanField(default=False)
    bedtype = models.CharField(max_length=30,choices=bed_type)
    description = models.CharField(max_length=200)
    
 
    def __str__(self):
        return str(self.room_no)



    