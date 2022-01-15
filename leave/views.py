from django.shortcuts import render,redirect
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
        if "accept" in request.POST:
            id1=request.POST.get("id")
            obj=leave.objects.get(id=id1)
            print("saving objects")
            obj.approve_leave()
            obj.save()
        if "reject" in request.POST:
            print("rejected")
        return redirect('/leave_request')
    leaves = leave.objects.all()
    pending_leaves = leave.objects.filter(is_approved=False)
    dep_leaves = leaves.filter(department=request.user.employee.get_department())
    pending_dep_leaves=dep_leaves.filter(is_approved=False)

    context = {
        "leaves": leaves,
        "pending_leaves": pending_leaves,
        "dep_leaves": pending_dep_leaves
    }
    return render(request,'Leave/LeaveRequest.html',context)

