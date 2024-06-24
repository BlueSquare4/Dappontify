from django.contrib import admin
from django.urls import path
from mainapp import views

urlpatterns = [
    path("home", views.home, name='home'),
    
]
