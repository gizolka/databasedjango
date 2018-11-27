from django.contrib import admin
from .models import Event, Activity, Attendance
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser
from django.contrib import admin
from django import forms

admin.site.register(Event)
admin.site.register(Activity)
admin.site.register(Attendance)

'''
# field attribute and exclude attribute necessary!
class EventAdminForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=Event.objects.order_by('username'))

    class Meta:
        model = Event

class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm

admin.site.register(EventAdmin)
'''
