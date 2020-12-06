from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
# Problem - Meeting Room Booking
#
# Specs:
# - View nearby meeting-room providers / coworks
# - Coworks' start and end times of the day varies
# - Booking to be done on an hourly basis
# - View availabilities of meeting-rooms with room info
#
# What is expected:
# - hosted application
# - codebase shared via Github
# - usage instructions if any

@login_required
def index(request):
    coworks = Cowork.objects.all()
    context={
      'coworks':coworks
    }
    return render(request,'cobook/index.html', context)

@login_required
def rooms(request):
    rooms = Room.objects.all()
    context={
      'rooms':rooms
    }
    return render(request,'cobook/rooms.html', context)

# def room(request):
#     coworks = Cowork.objects.all()
#     context={
#       'object':object
#     }
#     return render(request,'cobook/index.html', context)
