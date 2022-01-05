from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserRegistrationForm

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
        return render(request, 'Employee/Login.html', {'content': "/static/Employee/login.css"})

def Register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('/dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'Employee/Register.html', {'form':form})
