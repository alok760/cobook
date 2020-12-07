from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="home"),
    path('rooms/<int:id>/',views.rooms,name="rooms"),
    path('bookroom/<int:id>/',views.bookroom, name="bookrooms"),
    path('bookings',views.bookings, name="bookings")
]
