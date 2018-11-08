# timetable/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.db.models import Q
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Event, Activity, Attendance

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    login_url = 'login'


class TimetableListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'list.html'
    login_url = 'login'
    paginate_by = 6
    queryset = Event.objects.all()


    def get_queryset(self):
        order = self.request.GET.get('o','date')
        filter_val = self.request.GET.get('f', '')
        #new_context = Event.objects.filter(date__gte='2018-01-01', end_date__lte='2018-01-31')
        new_context = Event.objects.filter(Q(title__contains=filter_val) | Q(description__contains=filter_val)).order_by(order)
        return new_context

    def get_context_data(self, **kwargs):
        context = super(TimetableListView, self).get_context_data(**kwargs)
        context['o'] = self.request.GET.get('o', 'date')
        context['f'] = self.request.GET.get('f')
        return context


class TimetableDetailView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = 'view_event.html'
    login_url = 'login'

class TimetableCreateView(LoginRequiredMixin, CreateView):
    model = Event
    template_name = 'event_add.html'
    fields = ('title', 'type_of_event', 'date', 'end_date', 'type', 'duration', 'description')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TimetableUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    template_name = 'event_edit.html'
    fields = ('title', 'type_of_event', 'date', 'end_date', 'type', 'duration', 'description')
    login_url = 'login'
'''
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user !=self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
'''
class TimetableDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    template_name = 'event_delete.html'
    success_url = reverse_lazy('list')
    login_url = 'login'
'''
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user !=self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
'''
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
