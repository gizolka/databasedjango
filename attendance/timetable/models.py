#timetable/models.py
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
import datetime

class Activity(models.Model):
    SPEAKER = 'SP'
    ATTENDEE = 'AT'
    TRAINER = 'TR'
    ORGANIZER = 'OR'
    ACTIVITY_TYPE_CHOICES = (
        (SPEAKER, 'Speaker'),
        (ATTENDEE, 'Attendee'),
        (TRAINER, 'Trainer'),
        (ORGANIZER, 'Organizer')
    )
    type = models.CharField(
        max_length=50,
        choices=ACTIVITY_TYPE_CHOICES,
        default=SPEAKER
    )
    duration = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
#        return self.ACTIVITY_TYPE_CHOICES[self.type][1]
        return self.type in (self.SPEAKER, self.ATTENDEE)

    def get_absolute_url(self):
        return reverse('view_event')

class Event(Activity):
    CONFERENCE = 'CF'
    TRAINING = 'TR'
    WORKSHOP = 'WS'
    MEETING = 'ME'
    TYPE_OF_EVENT_CHOICES = (
        (CONFERENCE, 'Conference'),
        (TRAINING, 'Training'),
        (WORKSHOP, 'Workshop'),
        (MEETING, 'Meeting'),
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True,
    )
    title = models.CharField(max_length=64, blank=False)
    type_of_event = models.CharField(
        max_length=50,
        choices=TYPE_OF_EVENT_CHOICES,
        blank=False,
        default=CONFERENCE,
    )
    date = models.DateTimeField('event date')
    end_date = models.DateTimeField('event enddate')
    description = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_event', args=[str(self.id)])


'''
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        blank=False,
        default=None,
        related_name='activities',
    )
'''
    #user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=False, default=None)
    #description = models.TextField(max_length=1000, blank=True)

class Attendance(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='activities',
        null=True,
    )
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.event

    def get_absolute_url(self):
        return reverse('view_event')
