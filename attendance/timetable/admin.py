from django.contrib import admin
from .models import Event, Activity, Attendance


admin.site.register(Event)

admin.site.register(Activity)

admin.site.register(Attendance)

'''
class ActivityInline(admin.TabularInline):
    model = Activity
    extra = 0

class EventAdmin(admin.ModelAdmin):
    inlines = [
        ActivityInline,
    ]
'''
