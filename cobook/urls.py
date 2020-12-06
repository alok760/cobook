from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="home"),
    path('rooms/<int:id>/',views.rooms,name="rooms"),
    path('bookroom',views.bookroom, name="bookrooms")
]
