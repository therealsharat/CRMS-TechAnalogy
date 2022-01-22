from django.shortcuts import render, redirect
from Resignation.forms import ResigCreationForm
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from Resignation.models  import Resignation
import os
from django.conf import settings
from django.http import HttpResponse, Http404
# Create your views here.
def resignation_creation(request):
    if request.method=='POST':
        form=ResigCreationForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            Resig=form.save(commit=False)
            Resig.user=request.user
            Resig.save()
            return redirect('/dashboard')
    else:
        form=ResigCreationForm()
    return render(request,'Dashboard/Resignation.html')
def resignation_request(request):
    if request.method =="POST":
        id1 = request.POST.get("id")
        obj = Resignation.objects.get(id=id1)
        if "accept" in request.POST:
            obj.Approve()
        if "reject" in request.POST:
            obj.Reject()
        return redirect('Resignation_request')
    resignations = Resignation.objects.all()
    pending_resignations = resignations.filter(status="Pending")
    context = {
        "resignation":pending_resignations
    }
    return render(request, 'Resignation/ResignationRequest.html', context)

def resignation_status(request):
    resignation=Resignation.objects.all()
    resignation=resignation.filter(user=request.user)
    context={
        "resignation":resignation
    }
    return render(request,'Resignation/ResignationStatus.html',context)
def FileDownload(request):
    if request.method=='POST':
        file_name=request.POST.get('attachment')
        file_path=os.path.join(settings.MEDIA_ROOT,file_name)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response
        raise Http404
    else:
        form=ResigCreationForm()
    return render(request,'Dashboard/Resignation.html')
