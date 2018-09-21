from django.db import models
from django.conf import settings

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200)
    type_of_event = models.CharField(max_length=50, help_text='Enter the event type (e.g. conference, training, workshop)')
    date = models.DateTimeField('event date')
    end_date = models.DateTimeField('event enddate')
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('event-detail', args=[str(self.id)])

class Activity(models.Model):
    type = models.CharField(max_length=50, help_text='Enter either Speaker or Attendee')
    duration = models.DecimalField(max_digits=5, decimal_places=1, help_text='Enter your attendance time in hours')
    description = models.CharField(max_length=1000)

class Attendance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
