from django.urls import path
from ptfinderApp import views

app_name = 'ptfinder'

urlpatterns = [
    path('', views.index, name="index"),
    path('contactus/', views.contactus, name="contactus"),
    path('book/', views.book, name="book"),
    
]