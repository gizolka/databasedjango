from django.contrib import admin
from .models import Event, Activity, Attendance


class ActivityInline(admin.TabularInline):
    model = Activity
    extra = 0

class EventAdmin(admin.ModelAdmin):
    inlines = [
        ActivityInline,
    ]

admin.site.register(Event, EventAdmin)

admin.site.register(Activity)

admin.site.register(Attendance)
