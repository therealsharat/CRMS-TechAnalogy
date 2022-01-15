from django.shortcuts import render, redirect
from Resignation.forms import ResigCreationForm
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
# Create your views here.
def resignation(request):
    if request.method=='POST':

        form=ResigCreationForm(request.POST,request.FILES)
        if form.is_valid():
            Resig=form.save(commit=False)
            Resig.user=request.user
            Resig.save()
            return redirect('/dashboard')
    else:
        form=ResigCreationForm()
    return render(request,'Dashboard/Resignation.html')

