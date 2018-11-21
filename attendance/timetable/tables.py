from django.db.models import F
from .models import Event, Activity, Attendance
from django.db.models.functions import Length
import django_tables2 as tables

class EventTable(models.Table):
    user = tables.Table()
    title = tables.Table()
    type_of_event = tables.Table()
    date = tables.Table()
    end_date = tables.Table()
    type = tables.Table()
    duration = tables.Table()
    description = tables.Table()

    class Meta:
        model = Event

        def render_activity(self, record):
            return str(record.type)

        def order_activity(self, QuerySet, is_descending):
            QuerySet = QuerySet.annotate(F('type')).order_by(('-' if is_descending else ''))
            return (QuerySet, True)
