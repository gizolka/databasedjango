# timetable/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from formtools.wizard.views import SessionWizardView
from .forms import event, location, activity
import datetime
from .models import Event, Activity, Attendance


class HomePageView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'home.html'
    login_url = 'login'
    paginate_by = 12

    def get_queryset(self):
        order = self.request.GET.get('o', 'date')
        context = Event.objects.filter(user=self.request.user).order_by(order)
        return context


class TimetableListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'list.html'
    login_url = 'login'
    paginate_by = 10

# Sortable table columns
    def get_queryset(self):
        order = self.request.GET.get('o','date')
        filter_val = self.request.GET.get('f', '')
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
    fields = ('title', 'type_of_event', 'date', 'end_date', 'country', 'description', 'type', 'duration')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TimetableUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    template_name = 'event_edit.html'
    fields = ('title', 'type_of_event', 'date', 'end_date', 'country', 'description', 'type', 'duration')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user !=self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class TimetableDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    template_name = 'event_delete.html'
    success_url = reverse_lazy('list')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user !=self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

#Creating split forms across multiple Web pages
class EventWizard(SessionWizardView):
    template_name = "wizard_form.html"
    form_list = [event,location,activity]
    
    def done(self, form_list, form_dict, **kwargs):
        event       = form_dict['0']
        location    = form_dict['1']
        activity    = form_dict['2']

        if event.is_valid() and location.is_valid() and activity.is_valid():
            E = Event.objects.create(
                    user=self.request.user,
                    title=event.cleaned_data['title'],
                    type_of_event=event.cleaned_data['type_of_event'],
                    date=event.cleaned_data['date'],
                    end_date=event.cleaned_data['end_date'],
                    country=location.cleaned_data['country'],
                    description=location.cleaned_data['description'],
                    type=activity.cleaned_data['type'],
                    duration=activity.cleaned_data['duration']
                )
            E.save()
            
        return render(self.request, 'done.html', {
            'event' : event.cleaned_data,
            'location': location.cleaned_data,
            'activity': activity.cleaned_data,
        })

    def get(self, request, *args, **kwargs):
        try:
            return self.render(self.get_form())
        except KeyError:
            return super().get(request, *args, **kwargs)