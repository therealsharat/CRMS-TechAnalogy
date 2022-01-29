from django.shortcuts import render, redirect
from Resignation.forms import ResigCreationForm
from django.contrib.auth.models import User
from Resignation.models import Resignation
import os
from drive import Create_Service

from django.conf import settings
from django.http import HttpResponse, Http404
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload


# Create your views here.
def resignation_creation(request):
    if request.method == 'POST' and 'attachment' in request.FILES:
        form = ResigCreationForm(request.POST)
        file = request.FILES['attachment']
        service = Create_Service()
        folder_id ="1Ne_prxoAGYaQ43GsJy4mIvZvlg0Wg6ns"
        media = MediaFileUpload(file.temporary_file_path())
        file_metadata = {
            'name': '{0}'.format( request.user),
            'parents': [folder_id]
        }
        service.files().create(
            body=file_metadata,
            media_body=media

        ).execute()
        file.close()
        if form.is_valid():
            Resig = form.save(commit=False)
            Resig.user = request.user
            Resig.save()
            return redirect('/dashboard')
    else:
        form = ResigCreationForm()
    return render(request, 'Dashboard/Resignation.html')


def resignation_request(request):
    if request.method == "POST":
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
        "resignation": pending_resignations
    }
    return render(request, 'Resignation/ResignationRequest.html', context)


