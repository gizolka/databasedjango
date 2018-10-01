# timetable/views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .models import Event

from timetable.forms import EventForm
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
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'timetable/thanks.html', {'message': "Thanks"})
        else:
            return render(request, 'timetable/thanks.html', {'message': "Error"})

    else:
        form = EventForm()
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
