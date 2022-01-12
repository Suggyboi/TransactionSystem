from django.urls import path
from . import views

from .views import EventListView, EventCreateView
    

app_name = 'shop'

urlpatterns = [
    path('', views.allEveCat, name= 'allEveCat'),
    path('<uuid:category_id>/', views.allEveCat, name = 'events_by_category'),
    path('', EventListView.as_view(), name = 'event'),
    path('<uuid:event_id>/delete/', views.event_delete, name = 'delete'),
    path('organiser.html', EventCreateView.as_view(), name = 'event_create'),
    path('<uuid:category_id>/<uuid:event_id>/', views.event_detail, name = 'event_detail'),
    path('myevents', views.my_events, name='my_events'),
]
