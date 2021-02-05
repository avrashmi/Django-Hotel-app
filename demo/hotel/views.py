from django.shortcuts import render
from django.http import HttpResponse
from .models import Room,RoomType
from django.views.generic import ListView,DetailView
# Create your views here.

class Home(ListView):
    model = Room
    template_name ='home.html'



class DetailPage(DetailView):
    model = Room
    template_name ='detailPage.html'
        
    

