from django.shortcuts import render
from django.contrib.auth.models import User
from Employee.models import Employee
from django.contrib.auth.decorators import login_required
from leave.models import leave
from Resignation.models import Resignation
from django.db.models import Q

# Create your views here.

@login_required
def Dashboard(request):
    employees = request.user.employee
    resignations=Resignation.objects.all()
    pending_resignations=resignations.filter(status='Pending')

    # for technical head
    leaves = leave.objects.all()
    pending_leaves = leaves.filter(status="Pending")

    # for user
    user_leaves=leaves.filter(user=request.user)
    user_pending_leaves=user_leaves.filter(status="Pending")

    #for department heads

    dep_leaves = leaves.filter(department=request.user.employee.get_department())
    dep_leaves = dep_leaves.filter(~Q(user=request.user))
    dep_pending_leaves=dep_leaves.filter(status="Pending")

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
    employees = request.user.employee
    context = {
        'employees': employees
    }
    return render(request, 'Dashboard/Personal.html', context)

@login_required
def Leave(request):
    employees = request.user.employee
    context = {
        'employees': employees
    }
    return render(request, 'Dashboard/Leave.html', context)

@login_required
def resignation(request):
    employees = request.user.employee
    context = {
        'employees': employees
    }
    return render(request, 'Dashboard/Resignation.html', context)

@login_required
def Task(request):
    employees = request.user.employee
    employee=Employee.objects.all()
    employee = employee.filter(~Q(user=request.user))
    dep_employees = employee.filter(department__department_name=request.user.employee.get_department())
    dep_employees = dep_employees.filter(~Q(user=request.user))

    context = {
        'employees': employees,
        "employee": employee,
        "dep_employee": dep_employees
    }
    return render(request, 'Dashboard/Task.html', context)