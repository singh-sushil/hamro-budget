from django.contrib import admin
from django.urls import path
from matrix import views

urlpatterns = [
    path('signup/',views.home,name = 'home'),
]
