from django.forms import ValidationError
from webapp.models import Tasks
from django import forms
from django.core.validators import MinLengthValidator




def max_length_validator(string):
    if len(string) > 20:
        raise ValidationError('The max number of characters is 20')
    return string


def min_length_validator(string):
    if len(string) < 8:
        raise ValidationError('The minimum number of characters is 8')
    return



class TaskForm(forms.ModelForm):
    task = forms.CharField(validators=(min_length_validator, max_length_validator))

    class Meta:
        model = Tasks
        fields = ('task', 'description', 'type', 'status')
