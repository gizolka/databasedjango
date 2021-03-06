from django import forms
from timetable import mychoices
from django_countries.fields import CountryField

from .models import Activity, Event, Attendance

class event(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    type_of_event = forms.ChoiceField(initial='', 
        choices=mychoices.TYPE_OF_EVENT_CHOICES, 
        widget=forms.Select, 
        required=True,
    )
    date = forms.DateField(widget=forms.DateInput, required=True)
    end_date = forms.DateField(widget=forms.DateInput, required=True)

class location(forms.Form):
    country = forms.CharField(max_length=50, required=True)
    description = forms.CharField(widget=forms.Textarea, required=False) 

class activity(forms.Form):
    type = forms.ChoiceField(choices=mychoices.ACTIVITY_TYPE_CHOICES, required=True, initial='')
    duration = forms.ChoiceField(choices=mychoices.DURATION_CHOICES, required=True, initial='')
