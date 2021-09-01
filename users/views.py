from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django import forms
from .forms import RegisterUsers
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def user_register(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterUsers(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            data_username = form.cleaned_data['username']
            data_password = form.cleaned_data['password']
            user = User.objects.create_user(data_username, 'None', data_password)
            user.save()
            return render(request, 'users/index.html')
    else:
        form = RegisterUsers()
        
    return render(request, 'users/register.html', {'form': form})

def login_user(request):
    form = RegisterUsers(request.POST)
    if form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("ok")
            login(request, user)
            print("bien loguer")
            return render(request, 'users/index.html')
        else:
            pass
    else:
        messages.error(request, "Error")
    return render(request, 'users/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return render(request, 'users/logout.html')





    """
    user = authenticate(request, username=data_username, password=data_password)
    if user is not None:
    login(user)
    print("valide")
    return render(request, 'users/index.html')
    else:
    messages.error(request, "Error")            
    """
