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
    def save(self, commit=True):
        event = form(EventForm, self).save(commit=False)
        event.title = self.cleaned_data['title']
        event.type_of_event = self.cleaned_data['type_of_event']
        event.date = self.cleaned_data['date']
        event.end_date = self.cleaned_data['end_date']
        event.description = cleaned_data['description']

        if commit:
            event.save()
        return event


form = EventForm()

event = Event.objects.get(pk=1)
form = EventForm(instance=event)

class ActivityForm(forms.ModelForm):
        model = Activity
        fields = ['type', 'duration', 'description']

class AttendanceForm(forms.ModelForm):
        model = Attendance
        fields = ['user', 'event', 'activity']
