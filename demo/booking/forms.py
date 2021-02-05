from django import forms
from .models import Booking


class BookingForm(forms.Form):
    room_type =forms.IntegerField()
    from_date =forms.DateTimeField(widget=forms.TextInput(attrs={
        'type':'datetime-local'
    }))
    to_date =forms.DateTimeField(widget=forms.TextInput(attrs={
        'type':'datetime-local'
    }))


    
