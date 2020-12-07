from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from datetime import date, datetime
from math import sin, cos, sqrt, atan2, radians
import csv


# Create your views here.
# Problem - Meeting Room Booking
#
# Specs:
# - View nearby meeting-room providers / coworks
# - Coworks' start and end times of the day varies - done, validation remains
# - Booking to be done on an hourly basis - done
# - View availabilities of meeting-rooms with room info - done
#
# What is expected:
# - hosted application
# - codebase shared via Github
# - usage instructions if any

def distance_calc(lat1,lon1,lat2,lon2):
    R = 6373.0

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance

def sort_by_location(cws,zip):
    #breakpoint()
    distances = {}

    # try:
    with open('out.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    zipstr = str(zip) + '.0'

    for row in data:
        if row[0] == zipstr:
            lat1 = radians(float(row[1]))
            lon1 = radians(float(row[2]))
            break

    for cw in cws:

        zip1 = cw.zipcode
        zip1str = str(zip1) + '.0'

        for row in data:
            if row[0] == zip1str:
                lat2 = radians(float(row[1]))
                lon2 = radians(float(row[2]))
                break

        dist = distance_calc(lat1,lon1,lat2,lon2)
        distances[cw] = dist
    sorted_distances = dict(sorted(distances.items(), key=lambda x: x[1]))
    return list(sorted_distances.keys())
    breakpoint()

    # except:
    #     return cws

@login_required
def index(request):
    coworks = Cowork.objects.all()
    cws = []
    for cw in coworks:
        cws.append(cw)
    context={
      'coworks':cws
    }
    if request.method == 'POST':
        zip = request.POST["pin"]
        cws = sort_by_location(cws,zip)
        context={
          'zip':zip,
          'coworks':cws
        }
    return render(request,'cobook/index.html', context)

@login_required
def bookings(request):
    user = request.user
    bks = Booking.objects.filter(user_id=user.id)
    #breakpoint()
    context={
      'bks':bks
    }

    return render(request,'cobook/mybookings.html', context)

@login_required
def rooms(request,id):
    cowork = Cowork.objects.filter(id=id).last()
    rooms = cowork.room_set.all()
    context={
      'rooms':rooms
    }
    #breakpoint()
    return render(request,'cobook/rooms.html', context)

@login_required
def bookroom(request,id):

    if request.method == 'POST':

        if 'a_date' in request.POST:
            av_data = availability(request.POST['a_date'],id)
            not_empty = True
            # if len(av_data) >0:
            #     not_empty = True

            form = BookingForm()
            #breakpoint()
            context={
              'date':request.POST['a_date'],
              'form':form,
              'not_empty': not_empty,
              'availability':av_data
            }
            #breakpoint()
            return render(request, "cobook/booking.html", context)

        book = Booking()
        book.room = Room.objects.filter(id=id).last()
        book.user = request.user
        book.is_active = True
        form = BookingForm(request.POST, instance = book)

        if form.is_valid():
            av_data = availability(request.POST['date'],id)
            start_time = request.POST['start_time']
            end_time = request.POST['end_time']

            if not start_time < end_time:
                context={
                  'error_message':"Start Time must be less than End Time."
                }
                return render(request, "cobook/error_page.html", context)

            request_datetime = request.POST['date'] + " " + request.POST['start_time']

            rdate = datetime.strptime(request_datetime, '%Y-%m-%d %H:%M')
            now = datetime.now()


            if now > rdate:
                context={
                  'error_message':"Connot Book for past Date or Time."
                }
                return render(request, "cobook/error_page.html", context)


            for adata in av_data:
                s_time = adata[1]
                e_time = adata[2]
                # breakpoint()
                if start_time > s_time and start_time < e_time:
                    context={
                      'error_message':"Meeting Time collides with other Meetings."
                    }
                    return render(request, "cobook/error_page.html", context)

                if end_time > s_time and end_time < e_time:
                    context={
                      'error_message':"Meeting Time collides with other Meetings."
                    }
                    return render(request, "cobook/error_page.html", context)

            context={
              'message':"success"
            }
            form.save()
            return render(request, "cobook/booking_confirm.html", context)

        else:
            return render(request, "cobook/error_page.html")

    form = BookingForm()
    context={
      'form':form
    }
    data = availability(date.today(),1)
    #breakpoint()
    return render(request, "cobook/booking.html", context)




def availability(date, room_id):
    books = Booking.objects.filter(date=date)
    data = []
    for book in books:
        data.append([book.user.username, str(book.start_time)[:-3],str(book.end_time)[:-3]])
    return data






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
