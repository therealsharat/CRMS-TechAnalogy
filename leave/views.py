from django.shortcuts import render,redirect
from .forms import LeaveCreationForm
# Create your views here.
def leave_creation(request):
    if request.method=="POST":
        form=LeaveCreationForm(request.POST)
        Leave=form.save(commit=False)
        Leave.user=request.user
        Leave.save()
        return redirect('/dashboard')
    else:
        form=LeaveCreationForm()
    return render(request,'Dashboard/Leave.html')
