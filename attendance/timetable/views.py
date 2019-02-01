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
from .forms import EventForm1, EventForm2, EventForm3
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
    form_list = [EventForm1,EventForm2,EventForm3]
    
    def done(self, form_list, **kwargs):
        return render(self.request, 'done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })

    def get(self, request, *args, **kwargs):
        try:
            return self.render(self.get_form())
        except KeyError:
            return super().get(request, *args, **kwargs)