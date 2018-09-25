# timetable/forms.py
from django import forms
from .models import Event

class EventForm(forms.ModelForm):
  class Meta:
        model = Event
        fields = ['title','type_of_event', 'date', 'end_date', 'description']
