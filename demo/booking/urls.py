from django.urls import path
from  booking import views

urlpatterns =[
    #path('booking/', views.book ,name='Booking'),
    path('book/', views.BookingPage.as_view(), name ="bookingPage")

]