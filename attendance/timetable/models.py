#timetable/models.py

from django.urls import reverse
from django.db import models
from django.conf import settings

class Event(models.Model):
    title = models.CharField(max_length=200, default='')
    type_of_event = models.CharField(max_length=100, default='')
    date = models.DateTimeField('event date')
    end_date = models.DateTimeField('event enddate')
    description = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_event', args=[str(self.id)])

class Activity(models.Model):
    type = models.CharField(max_length=50, help_text='Enter either Speaker or Attendee')
    duration = models.DecimalField(max_digits=5, decimal_places=1, help_text='Enter your attendance time in hours')
    description = models.CharField(max_length=1000)

class Attendance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
