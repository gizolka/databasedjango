# timetable/views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .models import Event

from .forms import EventForm

def new_event(request):

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')

        else:
            form = EventForm()

        return render(request, 'event.html', {'form': form})


def index(request):
    query_request = Event.objects.all()
    template = loader.get_template('timetable/index.html')
    context = {
        'query_request': query_request,
    }
    return HttpResponse(template.render(context, request))

def links(request):
    return render(request, 'timetable/links.html', {})
