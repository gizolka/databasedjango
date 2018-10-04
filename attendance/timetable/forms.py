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
)

class EventForm(forms.Form):
    title = forms.CharField(required=True)
    type_of_event = forms.ChoiceField(
        required=True,
        choices=TYPE_OF_EVENT_CHOICES,
        )
    date = forms.DateTimeField(widget=forms.DateInput,required=True)
    end_date = forms.DateTimeField(widget=forms.DateInput, required=True)
    description = forms.CharField(widget=forms.Textarea, required=False)


class ActivityForm(forms.Form):
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
