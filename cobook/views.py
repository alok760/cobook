from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from datetime import date

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
def rooms(request,id):
    cowork = Cowork.objects.filter(id=id).last()
    rooms = cowork.room_set.all()
    context={
      'rooms':rooms
    }
    #breakpoint()
    return render(request,'cobook/rooms.html', context)


def bookroom(request,id):

    if request.method == 'POST':
        if 'a_date' in request.POST:
            breakpoint()
            data = availability(date.today(),1)
            #breakpoint()
            return render(request, "cobook/booking.html", context)

        book = Booking()
        book.room = Room.objects.filter(id=id).last()
        book.user = request.user
        book.is_active = True
        form = BookingForm(request.POST, instance = book)

        if form.is_valid():
            context={
              'message':"success"
            }
            form.save()
            return render(request, "cobook/booking_confirm.html", context)

        else:
            return render(request, "cobook/error_page.html")

    form = BookingForm()
    context={
      'room_schedule': None,
      'form':form
    }
    data = availability(date.today(),1)
    #breakpoint()
    return render(request, "cobook/booking.html", context)




def availability(date, room_id):
    books = Booking.objects.filter(date=date.today())
    data = []
    for book in books:
        data.append([book.user.username, str(book.start_time),str(book.end_time)])
    return data

def your_bookings():
    pass



# def bookroom(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             pass  # does nothing, just trigger the validation
#     else:
#         form = BookingForm()
#         context={
#           'form':form
#         }
#     return render(request, "cobook/booking.html", context)
