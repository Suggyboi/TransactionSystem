from django.shortcuts import render
from shop.models import Event
from django.db.models import Q

def searchResult(request):
    events = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        events = Event.objects.all().filter(Q(title__contains=query) | Q(description__contains=query))
    return render(request, 'search.html', {'query':query, 'events':events})