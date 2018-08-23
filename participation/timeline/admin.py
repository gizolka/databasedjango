from django.contrib import admin

# Register your models here.

from .models import Event, Attendance, Activity

admin.site.register(Event)

admin.site.register(Attendance)

admin.site.register(Activity)


