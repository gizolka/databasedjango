# timetable/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponseRedirect, HttpResponse
from .models import Event, Activity, Attendance
from django.urls import reverse

from timetable.forms import EventForm
from timetable.forms import ActivityForm

from django.views.generic import TemplateView


def home(request):
    numbers = [1,2,3,4,5]
    name = "Joanna Gizewska"

    links = '''
    <ul>
        <li><a href="/timetable/event/">Create an event</a></li>
    </ul>
    '''
    return render(request, 'timetable/home.html', { 'message': links })

def new_event(request):

    if request.method=='POST':
        form = EventForm(request.POST)
        if form.is_valid():
            # event = Event(title=form.cleaned_data['field-name'].....)
            # event.save()
            form.save()
            return render(request, 'timetable/view_event.html')
        else:
            return render(request, 'timetable/thanks.html', {'message': "Error"})
    else:
        form = EventForm()
    return render(request, 'timetable/event.html', {'form': form})

def view_event(request, event_id):
    object = get_object_or_404(Event,id=event_id)
    context = { 'o': object }

    return render(request, 'timetable/view_event.html', context)



def event_list(request):
    query_request = Event.objects.all()
    context = {
        'query_request': query_request,
    }
    return render(request, 'timetable/list.html', context)

def links(request):
    return render(request, 'timetable/links.html', {})

def new_activity(request):

    if request.POST:
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'timetable/thanks.html', {'message': "Thanks"})
        else:
            return render(request, 'timetable/thanks.html', {'message': "Error"})

    else:
        form = ActivityForm()
        return render(request, 'timetable/event.html', {'form': form})
