from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from django.core.urlresolvers import reverse


class EventForm(forms.Form):
        CONFERENCE = 'Conference'
        TRAINING = 'Training'
        WORKSHOP = 'Workshop'
        MEETING = 'Meeting'
        TYPE_OF_EVENT_CHOICES = (
            (CONFERENCE, 'Conference'),
            (TRAINING, 'Training'),
            (WORKSHOP, 'Workshop'),
            (MEETING, 'Meeting'),
        )

        SPEAKER = 'Speaker'
        ATTENDEE = 'Attendee'
        ACTIVITY_TYPE_CHOICES = (
            (SPEAKER, 'Speaker'),
            (ATTENDEE, 'Attendee'),
        )

        HALFDAY = '4 hours'
        ONEDAY = '8 hours'
        DURATION_CHOICES = (
            (HALFDAY, '4 hours'),
            (ONEDAY, '8 hours'),
        )
        user = forms.ModelChoiceFiled(
            get_user_model(),
            required=True,
        )
        title = forms.CharField(max_length=100, required=True)
        type_of_event = forms.ChoiceField(
            max_length=15,
            choices=TYPE_OF_EVENT_CHOICES,
            required=True,
        )
        date = forms.DateTimeField(widget=forms.DateInput)
        end_date = forms.DateTimeField(widget=forms.DateInput)
        description = forms.CharField(
            widget=forms.Textarea,
            max_length=500,
            required=False,
        )
        type = forms.ChoiceField(
            max_length=50,
            choices=ACTIVITY_TYPE_CHOICES,
            required=True,
        )
        duration = forms.ChoiceField(
            max_length=50,
            choices=DURATION_CHOICES,
            required=True,
        )



































''''
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


class AttendanceForm(forms.Form):
        user =
        event =
        activity =
'''
