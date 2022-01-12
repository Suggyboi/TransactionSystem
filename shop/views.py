from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Category, Event
from django.contrib.auth import authenticate, login
from .forms import EventForm

class EventListView(ListView):
    model = Event
    template_name = 'organiser.html'
    context_object_name = 'all_events_list'

class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('home')
    template_name = 'organiser.html'
    #fields = ['title', 'organiser', 'description', 'venue', 'startdate', 'enddate']

def allEveCat(request, category_id = None):
    my_categories = Category.objects.all()
    c_page = None
    events = None
    if category_id !=None:
        c_page = get_object_or_404(Category, id = category_id )
        events = Event.objects.filter(category = c_page, available = True)
    else:
        events = Event.objects.all().filter(available = True)

    return render(request, 'shop/category.html', {'category': c_page, 'events': events, 'categories': my_categories})

def event_delete(request, event_id):
    Event.objects.filter(id=event_id).delete()
    events = Event.objects.all
    return render(request, 'shop/category.html', {'events': events})

def event_detail(request,category_id,event_id):
    try:
       event = Event.objects.get(category_id=category_id,id=event_id)
    except Exception as e:
        raise e
    return render(request,'shop/event.html', {'event':event})

def my_events(request):
    events = Event.objects.all
    return render(request, 'my_events.html', {'events': events})

def error_404_view(request, exception):
    return render(request, 'not_found.html')
