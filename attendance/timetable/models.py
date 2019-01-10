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

    HALF = '4 hours'
    ONE = '8 hours'
    ONENHALF = '12 hours'
    TWO = '16 hours'
    TWONHALF = '20 hours'
    THREE = '24 hours'
    DURATION_CHOICES = (
        (HALF, '4 hours'),
        (ONE, '8 hours'),
        (ONENHALF, '12 hours'),
        (TWO, '16 hours'),
        (TWONHALF, '20 hours'),
        (THREE, '24 hours'),
    )
    type = models.CharField(
        max_length=50,
        choices=ACTIVITY_TYPE_CHOICES,
        blank=False,
        verbose_name="role",
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

    C3 = 'C3'
    CIRCL = 'CIRCL'
    CASES = 'CASES'
    DEPARTMENT_CHOICES = (
        (C3, 'C3'),
        (CIRCL, 'CIRCL'),
        (CASES, 'CASES'), 
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True,
    )
    department = models.CharField(
        max_length=50, 
        choices=DEPARTMENT_CHOICES, 
        blank=False, 
        default="default"
    )
    title = models.CharField(max_length=100, blank=False)
    type_of_event = models.CharField(
        max_length=15,
        choices=TYPE_OF_EVENT_CHOICES,
        blank=False,
        verbose_name="type",
    )
    date = models.DateTimeField('start', help_text = "dd/mm/yy")
    end_date = models.DateTimeField('end', help_text = "dd/mm/yy")
    country = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_event', args=[str(self.id)])

    class Meta:
        ordering = ['-date']

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
