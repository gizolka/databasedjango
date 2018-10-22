#timetable/models.py
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Event(models.Model):
    TYPE_OF_EVENT_CHOICES = (
        ('', '----'),
        ('CF', 'Conference'),
        ('TR', 'Training'),
        ('WS', 'Workshop'),
        ('ME', 'Meeting'),
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True,
    )
    title = models.CharField(max_length=200, blank=False)
    type_of_event = models.CharField(max_length=100, choices=TYPE_OF_EVENT_CHOICES, blank=False)
    date = models.DateTimeField('event date')
    end_date = models.DateTimeField('event enddate')
    description = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_event', args=[str(self.id)])

class Activity(models.Model):
    ACTIVITY_TYPE_CHOICES = (
        ('', '----'),
        ('SP','Speaker'),
        ('AT', 'Attendee'),
        ('TR','Trainer'),
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        blank=False,
        default=None,
        related_name='activities',
    )
    #user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=False, default=None)
    type = models.CharField(max_length=50, choices=ACTIVITY_TYPE_CHOICES)
    duration = models.DecimalField(max_digits=5, decimal_places=1, help_text='Enter your attendance time in hours eg. 1h')
    description = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('view_event')

class Attendance(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)

    def __str__(self):
        return self.event

    def get_absolute_url(self):
        return reverse('view_event')
