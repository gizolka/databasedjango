from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django import forms


urlpatterns = [
        path('', views.home, name='home'),
        path('home', views.home, name='home'),
        path('login', LoginView.as_view(template_name='timetable/login.html'), name='login'),
        path('event', views.new_event, name='timetable/event.html'),
]


# path('links', views.links, name='links')
