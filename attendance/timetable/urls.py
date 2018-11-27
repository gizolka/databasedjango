#timetable/urls.py
from django.urls import path
from .models import Event, Attendance, Activity
from .views import (
    TimetableListView,
    TimetableCreateView,
    TimetableDetailView,
    TimetableUpdateView,
    TimetableDeleteView,
)

urlpatterns = [
        path('', TimetableListView.as_view(), name='home'),
        path('event/list/', TimetableListView.as_view(), name='list'),
        path('event/add/', TimetableCreateView.as_view(), name='event_add'),
        path('event/<int:pk>/', TimetableDetailView.as_view(), name='view_event'),
        path('event/<int:pk>/edit/', TimetableUpdateView.as_view(), name='event_edit'),
        path('event/<int:pk>/delete/', TimetableDeleteView.as_view(), name='event_delete'),
]
