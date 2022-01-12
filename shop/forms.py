from django import forms
from .models import Event
from django.forms.widgets import DateInput

'''Event Creation Form'''
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'category', 'organiser', 'description', 'venue', 'image', 'startdate', 'starttime', 'enddate', 'endtime', 'price', 'stock')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'organiser': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'venue': forms.TextInput(attrs={'class': 'form-control'}),
            'startdate': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'enddate': forms.SelectDateWidget(attrs={'class': 'form-control'}),
        }


