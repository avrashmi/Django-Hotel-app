from django.shortcuts import render
from .models import Booking,Registertion
from hotel.models import Room
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.

from .forms import BookingForm


'''def book(request):
    if request.POST:
        from_post= request.POST.get('from_date')
        to = request.POST.get('to_date')
        room_count = request.POST.get('room_type')
        print(from_post,to)
        # post_data.objects.filter(from_data__gte )
        # to.objects.filter(to_date__lte =0)
        booking = Booking.objects.filter(from_date__gte =from_post , to_date__lte =to)

        booking_count = booking.count()
        room_total = Room.objects.count() 
        print(f" bookings: {booking_count}")
        print(f" Total Rooms: {room_total}")
    context ={'form':BookingForm, 'booking_count':booking_count, 'room_total':room_total}

    return render(request, 'booking.html',context)'''

class BookingPage(FormView):
    form_class =BookingForm 
    template_name ='booking.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['booking_count'] = 'booking_count'
        context['room_total'] ='room_total'
        
        return context
    
    
    def form_valid(self,form):
        booking = Booking.objects.filter(from_date__gte =form.cleaned_data['from_date'] , to_date__lte =form.cleaned_data['to_date'])

        booking_count = booking.count()
        room_total = Room.objects.count() 
        print(f" bookings: {booking_count}")
        print(f" Total Rooms: {room_total}")
        messages.add_message(self.request,messages.INFO,'rooms are available')

        return super().form_valid(form)
        

    def get_success_url(self):
    
        return reverse_lazy('bookingPage')

















