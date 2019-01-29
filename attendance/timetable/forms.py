from django import forms
from timetable import mychoices

from .models import Activity, Event, Attendance

class EventForm1(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    type_of_event = forms.ChoiceField(choices=mychoices.TYPE_OF_EVENT_CHOICES, 
        widget=forms.Select, 
        required=True,
    )
    date = forms.DateField(widget=forms.DateInput, 
        required=True, 
        USE_L10N=False, 
        input_formats="%d/%m/Y",
    )
    end_date = forms.DateField(widget=forms.DateInput,
        required=True, 
        USE_L10N=False, 
        input_formats="%d/%m/Y",
    )

class EventForm2(form.Form):
    country = forms.CharField(max_length=50, required=True)
    description = forms.CharField(widget=forms.Textarea) 

class EventForm3(form.Form):
    type = forms.CharField(max_length=50, required=True)
    duration = forms.DurationField(required=True)
