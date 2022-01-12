from django.contrib import admin
from .models import Category, Event

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, CategoryAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'description','organiser', 'venue', 'price', 'startdate', 'starttime', 'enddate', 'endtime', 'stock', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    list_per_page = 20

admin.site.register(Event,EventAdmin)

