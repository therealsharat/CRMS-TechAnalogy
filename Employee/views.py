from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            messages.success(request, "There was an error logging in, Try Again")
            return redirect('/')
    else:
        return render(request, 'Employee/Login.html', {'content': "/static/login.css"})
