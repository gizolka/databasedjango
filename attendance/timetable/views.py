# timetable/views.py

from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Event

# decorator login required


class TimetableListView(ListView):
    model = Event
    template_name = 'list.html'

class TimetableDetailView(DetailView):
    model = Event
    template_name = 'view_event.html'

class TimetableCreateView(CreateView):
    model = Event
    template_name = 'event_add.html'
    fields = '__all__'

class TimetableUpdateView(UpdateView):
    model = Event
    template_name = 'event_edit.html'
    fields = '__all__'

class TimetableDeleteView(DeleteView):
    model = Event
    template_name = 'event_delete.html'
    success_url = reverse_lazy('list')


'''
def home(request):
    numbers = [1,2,3,4,5]
    name = "Joanna Gizewska"

    links =
    <ul>
        <li><a href="/timetable/event/">Create an event</a></li>
    </ul>

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
'''
