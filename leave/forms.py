from django import forms
from .models import *

CHOICES=(('sick','sick'),('casual','casual'),('emergency','emergency'),("study",'study'))

class LeaveCreationForm(forms.ModelForm):
    startdate=forms.DateField()
    enddate=forms.DateField()
    reason=forms.CharField(max_length=100)
    leavetype=forms.ChoiceField(choices = CHOICES,
                       widget=forms.Select(attrs={'class': 'nice-select rounded'}),
                       )
    department=forms.CharField(max_length=30)
    class Meta:
        model =leave
        fields=['startdate','enddate','reason','leavetype','department']