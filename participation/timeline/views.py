from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

from .models import Event

def index(request):

    query_results = Event.objects.all()
    template = loader.get_template('home.html')
    context = {
        'query_results': query_results,
    }
    return HttpResponse(template.render(context, request))

def test(request, test_1):
    return HttpResponse("My test input %s." % test_1)

#def login(request):
    #return render(request, 'registration/login.html', {})
