from django.contrib import admin
from .models import Event, Activity, Attendance, UserProfile
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Event)
admin.site.register(Activity)
admin.site.register(Attendance)
