from django import forms
from .models import *
from django.contrib.auth.models import User
from .models import Task


class TaskAssignForm(forms.ModelForm):
    task_title = forms.CharField(max_length=30)
    assigned_to = forms.IntegerField()
    assign_date = forms.DateField()
    deadline = forms.DateField()
    task_description = forms.CharField(max_length=255)


    class Meta:
        model = Task
        fields = ['assign_date', 'assigned_to','deadline', 'task_title', 'task_description']
