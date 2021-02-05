from django.db import models
from hotel.models import Room,RoomType
# Create your models here.

class Booking(models.Model):
    room_type =models.ForeignKey(Room, on_delete=models.CASCADE)
    from_date =models.DateTimeField()
    to_date =models.DateTimeField()
    price =models.DecimalField(max_digits=5, decimal_places=2)


    def __str__(self):
        return str(self.room_type)


class Registertion(models.Model):
    booking =models.ForeignKey(Booking, on_delete=models.CASCADE)
    




    





