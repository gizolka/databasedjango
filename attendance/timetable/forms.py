# timetable/forms.py
from django import forms
from django.db import models
from django.contrib.auth.forms import User
from django.forms import ModelForm
from timetable.models import Event, Activity, Attendance

class EventForm(forms.ModelForm):
    title = forms.CharField(required=True)
    type_of_event = forms.CharField(required=True)
    date = forms.DateTimeField(required=True)
    end_date = forms.DateTimeField(required=True)
    description = forms.CharField(required=False)

    class Meta:
        model = Event
        fields = {
            'title',
            'type_of_event',
            'date',
            'end_date',
            'description'
        }


form = EventForm()

event = Event.objects.get(pk=1)
form = EventForm(instance=event)

class ActivityForm(forms.ModelForm):
        model = Activity
        fields = ['type', 'duration', 'description']

class AttendanceForm(forms.ModelForm):
        model = Attendance
        fields = ['user', 'event', 'activity']
