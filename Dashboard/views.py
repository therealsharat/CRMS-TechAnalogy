from django.shortcuts import render
from Employee.models import Employee
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def Dashboard(request):
    return render(request, 'Dashboard/Dashboard.html')

@login_required
def Personal(request):
    context = {
        'employee':Employee.objects.all()
    }
    return render(request, 'Dashboard/Personal.html')

@login_required
def Leave(request):
    return render(request, 'Dashboard/Leave.html')

@login_required
def Resignation(request):
    return render(request, 'Dashboard/Resignation.html')

@login_required
def Task(request):
    return render(request, 'Dashboard/Task.html')
