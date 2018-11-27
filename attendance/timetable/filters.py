# filters.py

import django_filters
from .models import Event, Activity, Attendance

class EventListFilter(django_filters.FilterSet):
    model = Event
    fields = ['user', 'title', 'type_of_event', 'date', 'end_date', 'type', 'duration', 'description']
    order_by = ['pk']
