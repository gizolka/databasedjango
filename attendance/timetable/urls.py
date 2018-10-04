from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django import forms


urlpatterns = [
        path('', views.home, name='home'),
        #path('logout'), LogoutView.as_view(template_name='timetable/logout.html', name='logout'),
        path('login/', LoginView.as_view(template_name='timetable/login.html'), name='login'),
        path('events/', views.event_list, name='events'),
        path('event/add/', views.new_event, name='event'),
        path('event/<int:event_id>/', views.view_event, name=' '),
        path('activity/add/', views.new_activity, name='activity'),
]


# path('links', views.links, name='links')
