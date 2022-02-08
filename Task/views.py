from django.shortcuts import render, redirect
from Employee.models import Employee
from .forms import TaskAssignForm
from drive import Create_Service
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from django.contrib.auth.models import User
from .models import Task
from django.core.mail import send_mail


# Create your views here.

def task_creation(request):
    if request.method == "POST":
        form = TaskAssignForm(request.POST)
        username = User.objects.get(pk=request.POST.get("assigned_to")).username
        user=User.objects.get(pk=request.POST.get("assigned_to"))
        folder_id = folder(request)
        if 'attachment' in request.FILES:
            service = Create_Service()
            file = request.FILES['attachment']
            media = MediaFileUpload(file.temporary_file_path())
            file_metadata = {
                'name': '{0}-{1}'.format(username, request.POST.get("task_title")),
                'parents': [folder_id]
            }
            res=service.files().create(
                body=file_metadata,
                media_body=media

            ).execute()
            file.close()
        list1=[]
        list1.append(user.employee.email)
        print(list1)
        Leave = form.save(commit=False)
        Leave.user = request.user
        Leave.save()
        send_mail("Task assigned - {0}".format(request.POST.get("task_title")),'You have been '
                       ' assigned task by {0} \n task link {url}'.format(request.user,url='https://drive.google.com/open?id=' + res.get('id')),
                  'technical.techanalogy@gmail.com',list1,fail_silently=False)

        return redirect('/dashboard')
    else:
        form = TaskAssignForm()
    return render(request, 'Dashboard/Task.html')


def folder(request):
    if request.user.employee.get_role() == "TechnicalHead":
        if User.objects.get(pk=request.POST.get("assigned_to")).employee.get_role() == "DomainHead" or "TechnicalSupervisor":
            return "1Li16l6YCbNRooyPb52oYry0IGjT2qiUE"
        else:
            return "1gV5Huee4E3vAL0hBDhg78qUeyS2ANhHf"
    if request.user.employee.get_role() == "TechnicalSupervisor":
        if User.objects.get(pk=request.POST.get("assigned_to")).employee.get_role() == "DomainHead":
            return "1IQIU2KKVWX6bghZmbM_SKyBPc5yYvKZ6"
        else:
            return "1lK3MnKs04B_AKyivskZp5ivTaHQJi-34"

    elif (request.user.employee.get_department() == "IoT"):
        return "1n8hUWAclWFpy-3dU1gHdEcsdWBdOrHPC"
    elif (request.user.employee.get_department() == "Mechanical"):
        return "1s14gD978MQ_7nxeOdnmoT9e6OAfeuqDX"
    elif (request.user.employee.get_department() == "Electrical"):
        return "1mygPSQivArjaOZMkkmshGBh9N3PqeyBe"
    elif (request.user.employee.get_department() == "Electronics"):
        return "1CgxO4UnYUyA1yXuWloc9xv6bq8YfiwCA"
    elif (request.user.employee.get_department() == "TechnicalManagement"):
        return "1AJ5gPeqeGlx8glmydv3Lz5jLBoeXabrj"
    elif (request.user.employee.get_department() =="Design"):
    	return "1mqWELsUw1DuWT1cKpH0j-Lqk8hQ-c7Oi"


def task_status(request):
    tasks = Task.objects.all()
    my_tasks = tasks.filter(assigned_to=request.user.id)
    assigned_tasks = tasks.filter(user=request.user)
    my_tasks = reversed(list(my_tasks))
    context = {
        "my_tasks": my_tasks

    }
    return render(request, 'Task/TaskStatus.html', context)


def task_submission(request):

    if "attachment" in request.FILES:
        list1=[]
        sumbmission = request.FILES['attachment']
        user = User.objects.get(pk=request.POST.get("user"))
        service = Create_Service()
        task = Task.objects.get(pk=request.POST.get("task"))
        folder_id = folder_sub(user)
        media = MediaFileUpload(sumbmission.temporary_file_path())
        file_metadata = {
            'name': '{0} -{1}'.format(task.task_title, request.user),
            'parents': [folder_id]
        }
        list1.append(user.employee.email)
        res=service.files().create(
            body=file_metadata,
            media_body=media

        ).execute()
        sumbmission.close()
    task = Task.objects.get(pk=request.POST.get("task"))
    task.close_task()
    if "attachment" in request.FILES:
        send_mail("Task submitted- {0}".format(task.task_title), '{0} has  successfully submitted task '
            '\n submission link {url}'.format(request.user,
             url='https://drive.google.com/open?id=' + res.get('id')),
                  'technical.techanalogy@gmail.com', list1, fail_silently=False)
    else :
        send_mail("Task submitted- {0}".format(task.task_title), '{0} has  successfully submitted task '
                .format(request.user),'technical.techanalogy@gmail.com', list1, fail_silently=False)

    return redirect('/task/task_status/')


def folder_sub(user):
    if user.employee.get_role() == "TechnicalHead":
        return "1G57kvul0L8BpKJPz-xpzOak8o-QoSyyY"
    elif (user.employee.get_role() == "TechnicalSupervisor"):
        return "12iaitDku5addx9bpq0Hm4GvkvnSNL6yA"
    elif (user.employee.get_department() == "IoT"):
        return "1rXp39nTMDZF1cLGrCYp539-G_6lJ_3Ny"
    elif (user.employee.get_department() == "Mechanical"):
        return "12rnnlB9Dm7RrejIr5YoQdndQn4ubyIWN"
    elif (user.employee.get_department() == "Electrical"):
        return "1ah5cv8zOWo_r7hPOs9RhWI-Yt6oqdX2V"
    elif (user.employee.get_department() == "Electronics"):
        return "1sfnNIad7dAV2PIyFQx5GUBwMcru8Ddg0"
    elif (user.employee.get_department() == "TechnicalManagement"):
        return "1-nCj91IzB0yJvZmhccwzMh0VsSXXYXN_"
    elif (user.employee.get_department() =="Design"):
        return  "1dDcENPaqR0p9tG_v81pOhVWJPE54Ktfw"






def task_assigned(request):
    tasks = Task.objects.all()
    assigned_tasks = tasks.filter(user=request.user)
    assigned_tasks = reversed(list(assigned_tasks))
    context = {
        "tasks": assigned_tasks

    }
    return render(request, 'Task/TaskAssigned.html', context)
