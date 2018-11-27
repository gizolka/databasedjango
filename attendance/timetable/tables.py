from .models import Event, Activity, Attendance
import django_tables2 as tables
from django_tables2.utils import A

class EventTable(tables.Table):
    user_name = tables.LinkColumn('event-detail', args=[A('pk')])
    user_email = tables.LinkColumn('event-detail', args=[A('pk')])
    user_duration = tables.LinkColumn('event_detail', args=[A('pk')])
    user_role = tables.LinkColumn('event_detail', args=[A('pk')])

    class Meta:
        model = Event
        fields = ('user', 'title', 'type_of_event', 'date', 'end_date', 'type', 'duration', 'description')
        attr = {"class": "table-striped table-bordered"}
        empty_text = "There are noresults matching the search criteria"

    
