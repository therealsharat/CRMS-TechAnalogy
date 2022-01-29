from django import forms
from .models import *

class ResigCreationForm(forms.ModelForm):
    Termination_date=forms.DateField()
    reason=forms.CharField(max_length=150)
    applied_date=forms.DateField()
    class Meta:
        model=Resignation
        fields=('Termination_date','reason','applied_date')

