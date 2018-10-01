import datetime
from django import forms
from django.db import models
from django.contrib.auth.forms import User
from django.forms import ModelForm
from timetable.models import Event, Activity, Attendance

TYPE_OF_EVENT_CHOICES = (
    ('CF', 'Conference'),
    ('TR', 'Training'),
    ('WS', 'Workshop'),
)

class EventForm(forms.ModelForm):
    title = forms.CharField(required=True)
    type_of_event = forms.ChoiceField(
        required=True,
        choices=TYPE_OF_EVENT_CHOICES,
        )
    date = forms.DateTimeField(widget=forms.DateTimeInput,required=True)
    end_date = forms.DateTimeField(widget=forms.DateTimeInput, required=True)
    description = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Event
        fields = [
            'title',
            'type_of_event',
            'date',
            'end_date',
            'description'
        ]


'''
class ActivityForm(forms.ModelForm):
        model = Activity
        fields = ['type', 'duration', 'description']

class AttendanceForm(forms.ModelForm):
        model = Attendance
        fields = ['user', 'event', 'activity']

'''
