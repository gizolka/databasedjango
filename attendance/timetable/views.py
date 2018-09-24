# timetable/views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Event

def home(request):
    query_request = Event.objects.all()
    template = loader.get_template('timetable/home.html')
    context = {
        'query_request': query_request,
    }
    return HttpResponse(template.render(context, request))
