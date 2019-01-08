#timetable/models.py
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
import datetime

class Activity(models.Model):
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
    type = models.CharField(
        max_length=50,
        choices=ACTIVITY_TYPE_CHOICES,
        blank=False,
    )
    duration = models.CharField(
        max_length=50,
        choices=DURATION_CHOICES,
        blank=False,
    )

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('view_event')

class Event(Activity):
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
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True,
    )
    title = models.CharField(max_length=100, blank=False)
    type_of_event = models.CharField(
        max_length=15,
        choices=TYPE_OF_EVENT_CHOICES,
        blank=False,
    )
    date = models.DateTimeField('event date', help_text = "dd/mm/yy")
    end_date = models.DateTimeField('event enddate', help_text = "dd/mm/yy")
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_event', args=[str(self.id)])

    class Meta:
        ordering = ['-date']

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
