#timetable/admin.py
from django.contrib import admin
from .models import Event, Activity, Attendance
# Register your models here.

admin.site.register(Event)
admin.site.register(Activity)
admin.site.register(Attendance)
