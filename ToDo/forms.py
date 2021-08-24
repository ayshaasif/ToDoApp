from django import forms
from .models import Reminder
from django.forms import DateTimeField
from django.contrib.admin import widgets
from django.forms.widgets import DateInput,TimeInput


class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        widgets = {
            'Date': DateInput(attrs={'type':'date'}),
            'Time': TimeInput(attrs={'type':'time'})
        }
        fields = '__all__'






