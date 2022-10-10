from dataclasses import fields
from webapp.models import Tasks
from django import forms




class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('task', 'description', 'type', 'status')
