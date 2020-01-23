from django.contrib import admin
from django.urls import path
from matrix import views

urlpatterns = [
    path('',views.home,name = 'home'),
    path('register/',views.register,name='regiter'),
    path('cregister/',views.cregister,name='cregister'),
    path('cregister/save/',views.cregister,name='cregister1'),
    path('official-login/',views.officiallogin,name='official_login'),
    path('user-login/',views.userlogin,name = 'userlogin'),
]
