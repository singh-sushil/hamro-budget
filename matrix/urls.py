from django.contrib import admin
from django.urls import path,re_path
from matrix import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name = 'home'),
    path('register/',views.register,name='regiter'),
    path('cregister/',views.cregister,name='cregister'),
    path('cregister/save/',views.cregister,name='cregister1'),
    path('official-login/',views.officiallogin,name='official_login'),
    path('user-login/',views.userlogin,name = 'userlogin'),
    #path('search/',views.search,name = 'search'),
    path('province1/',views.province1,name = 'province'),
    path('jhapa/',views.jhapa,name = 'jhapa'),
    path('jhapa/jhapagaunpalika/',views.jhapagaupalika,name = 'jhapagaupalika'),
    path('jhapa/jhapagaunpalika/feedback/',views.jhapagaupalika,name = 'feedback'),
    path('jhapa/jhapagaunpalika/drinking/feedback/',views.drinking,name = 'drinking'),
    path('jhapa/jhapagaunpalika/drinking/',views.drinking,name = 'drinking'),
    #re_path(r'(?P<username>\w+)/$',views.search,name='intro'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
