from django.shortcuts import render
from django.contrib.auth.models import User
from Employee.models import Employee
from django.contrib.auth.decorators import login_required
from leave.models import leave
from Resignation.models import Resignation

# Create your views here.

@login_required
def Dashboard(request):
    employees = Employee.objects.all()
    resignations=Resignation.objects.all()
    pending_resignations=Resignation.objects.filter(is_approved=False)
    #for user

    user_leaves=leave.objects.filter(user=request.user)
    user_pending_leaves=user_leaves.filter(is_approved=False)

    #for technical head

    leaves=leave.objects.all()
    pending_leaves=leaves.filter(is_approved=False)


    #for department heads

    dep_leaves = leave.objects.filter(department=request.user.employee.get_department())
    dep_pending_leaves = leaves.filter(is_approved=False)

    context = {
        'employees': employees,
        'user_pending_leaves':user_pending_leaves.count(),
        'user_leaves': user_leaves.count(),
        'leaves': leaves.count(),
        'pending_leaves': pending_leaves.count(),
        'dom_leaves': dep_leaves.count(),
        'dom_pending_leaves': dep_pending_leaves.count(),
        'resignations': resignations.count(),
        'pending_resignations': pending_resignations.count()

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
def resignation(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'Dashboard/Resignation.html', context)

def Task_View(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'Dashboard/Task_View.html', context)

@login_required
def Task(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'Dashboard/Task.html', context)
