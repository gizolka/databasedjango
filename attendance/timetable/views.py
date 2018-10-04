# timetable/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .models import Event, Activity
import logging

from timetable.forms import EventForm
from timetable.forms import ActivityForm

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'timetable/home.html'

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

    if request.POST:
        form = EventForm(request.POST)
        logging.warning(form)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'timetable/thanks.html', {'message': "Success"})
        else:
            return render(request, 'timetable/thanks.html', {'message': "Error"})
    else:
        form = EventForm()
        return render(request, 'timetable/event.html', {'form': form})

def view_event(request, event_id):
    try:
      object = Event.objects.get(id=event_id)
      template = loader.get_template('timetable/list1.html')
      context = {
        'object': object
      }
    except Event.DoesNotExist:
      object = None
    return redirect('/events/event_id/')

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

def event_list(request):
    query_request = Event.objects.all()
    template = loader.get_template('timetable/list.html')
    context = {
        'query_request': query_request,
    }
    return HttpResponse(template.render(context, request))

def links(request):
    return render(request, 'timetable/links.html', {})
