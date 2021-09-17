from products.models import Categories, Product
from products.forms import NameForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django import forms
from .forms import RegisterUsers
from django.http import HttpResponse
from django.urls import reverse

def index(request):
    return render(request, 'users/index.html')

def user_register(request):
    if request.method == 'POST':
        form = RegisterUsers(request.POST)
        if form.is_valid():
            data_username = form.cleaned_data['username']
            data_email = form.cleaned_data['email']
            data_password = form.cleaned_data['password']
            user = User.objects.create_user(data_username, data_email, data_password)
            user.save()
            return redirect('/')
    else:
        form = RegisterUsers()
        
    return render(request, 'users/register.html', {'form': form})

def login_user(request):
    form = RegisterUsers(request.POST)
    if form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = authenticate(request, username=username, email=email, password=password)
        if user is not None:
            print("ok")
            login(request, user)
            print("bien loguer")
            return redirect('/')
        else:
            pass
    else:
        messages.error(request, "Error")
    return render(request, 'users/login.html', {'form': form})

def user_account(request):
    form_prod = NameForm(request.POST)
    return render(request, 'users/user_account.html', {'form': form_prod})

def logout_user(request):
    logout(request)
    return redirect('/')
