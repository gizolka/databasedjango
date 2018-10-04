import datetime
from django import forms
from django.db import models
from django.contrib.auth.forms import User
from django.forms import ModelForm
from timetable.models import Event, Activity, Attendance

TYPE_OF_EVENT_CHOICES = (
    ('', '----'),
    ('CF', 'Conference'),
    ('TR', 'Training'),
    ('WS', 'Workshop'),
    ('ME', 'Meeting'),
)

ACTIVITY_TYPE_CHOICES = (
    ('', '----'),
    ('SP', 'Speaker'),
    ('AT', 'Attendee'),
    ('TR', 'Trainer'),
)

class EventForm(forms.ModelForm):
    title = forms.CharField()
    type_of_event = forms.ChoiceField(
        choices=TYPE_OF_EVENT_CHOICES,
    )
    date = forms.DateTimeField(
        widget=forms.DateInput,
    )
    end_date = forms.DateTimeField(
        widget=forms.DateInput,
    )
    description = forms.CharField(
        required=False,
    )

    class Meta:
        model = Event
        fields = {
            'title',
            'type_of_event',
            'date',
            'end_date',
            'description'
        }

class ActivityForm(ModelForm):
    type = forms.ChoiceField(
        required=True,
        choices=ACTIVITY_TYPE_CHOICES,
    )
    duration = forms.TimeField(
        widget=forms.TimeInput(format='%H:%M'),
        required=True
    )

'''
class AttendanceForm(forms.Form):
        user =
        event =
        activity =
'''
