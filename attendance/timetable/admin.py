from django.contrib import admin
from .models import Event, Activity, Attendance
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser
from django.contrib import admin
from django import forms

admin.site.register(Event)
admin.site.register(Activity)
admin.site.register(Attendance)

