# timetable/views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .models import Event

from timetable.forms import EventForm

def home(request):
    numbers = [1,2,3,4,5]
    name = "Joanna Gizewska"

    args = {'myName': name, 'numbers': numbers}
    return render(request, 'timetable/home.html', args)


def new_event(request):

    if request.POST:
        a=1/0
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            a=1/0
            return render(request, 'timetable/thanks.html', {'message': "Thanks"})
        else:
            a=1/0
            return render(request, 'timetable/thanks.html', {'message': "Error"})

    else:
        form = EventForm()
        return render(request, 'timetable/event.html', {'form': form})

'''
def index(request):
    query_request = Event.objects.all()
    template = loader.get_template('timetable/index.html')
    context = {
        'query_request': query_request,
    }
    return HttpResponse(template.render(context, request))

def links(request):
    return render(request, 'timetable/links.html', {})
'''
