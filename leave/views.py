from django.shortcuts import render, redirect
from .forms import LeaveCreationForm
from leave.models import *

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

def LeaveRequest(request):
    if request.method =="POST":
        id1 = request.POST.get("id")
        obj = leave.objects.get(id=id1)
        if "accept" in request.POST:
            obj.approve_leave()
        if "reject" in request.POST:
            obj.reject_leave()
        return redirect('leave_request')
    leaves = leave.objects.all()
    pending_leaves = leave.objects.filter(status="Pending")
    dep_leaves = leaves.filter(department=request.user.employee.get_department())
    pending_dep_leaves=dep_leaves.filter(status="Pending")

    context = {
        "leaves": leaves,
        "pending_leaves": pending_leaves,
        "dep_leaves": pending_dep_leaves
    }
    return render(request,'Leave/LeaveRequest.html',context)

def leave_status(request):
    leaves=leave.objects.all()
    my_leaves=leaves.filter(user=request.user)
    my_leaves=reversed(list(my_leaves))
    context={
        "my_leaves":my_leaves
    }
    return render(request,'Leave/LeaveStatus.html',context)