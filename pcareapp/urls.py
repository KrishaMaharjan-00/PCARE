from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('home',views.home, name='home'),
    path('home2',views.home2, name='home2'),
    path('about',views.index, name='about'),
    path('login',views.login, name='login'),
    path('contact',views.contact, name='contact'),
    path('healthy_diet',views.health, name='healthy_diet'),
    path('pbook',views.pbook, name='pbook'),
    path('awareness',views.awareness, name='awareness'),
    path('exercises',views.exercises, name='exercises'),
    path('vitamins',views.vitamins, name='vitamins'),
    path('mental',views.mental, name='mental'),
    path("message",views.message, name='message'),
    path('msg1',views.message1, name='message1'),
    path('msg2',views.message2, name='message2'),
    path('notification',views.notification, name='notification'),
    path('pressure',views.pressure, name='pressure'),
    
    
    
]
