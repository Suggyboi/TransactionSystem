from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.forms.widgets import DateInput

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username', 'dob', 'email', 'is_organiser']
        labels = {
            'dob' : ('Date of Birth'),
            'is_organiser' : ('Organiser Account')
        }
        widgets = {
            'dob': DateInput(attrs={'type': 'date'})
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = UserChangeForm.Meta.fields