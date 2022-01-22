from django import forms
from .models import *
from django.contrib.auth.models import User

UserList = []
for i in User.objects.all():
    UserList[i] = i.username

#ENUM
for j in UserList:
    UserChoices = (
        (UserList[i], UserList[i])
    )

class TaskAssignForm(forms.ModelForm):
    users = forms.ChoiceField(choices = UserChoices, widget=forms.Select(attrs={'class': 'nice-select rounded'}), )
    assign_date = forms.CharField()
    deadline = forms.DateField
    task_title = forms.CharField(max_length=30)
    task_description = forms.CharField(max_length=255)
    department = forms.CharField(max_length=30)

    class Meta:
        model = Task
        fields=['users', 'assign_date', 'deadline', 'task_title', 'task_description', 'department']
