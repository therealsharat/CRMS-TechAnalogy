from django.shortcuts import render
from django.contrib.auth.models import User
from Employee.models import Employee
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def Dashboard(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'Dashboard/Dashboard.html', context)

@login_required
def Personal(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'Dashboard/Personal.html', context)

@login_required
def Leave(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'Dashboard/Leave.html', context)

@login_required
def Resignation(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'Dashboard/Resignation.html', context)

@login_required
def Task(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'Dashboard/Task.html', context)