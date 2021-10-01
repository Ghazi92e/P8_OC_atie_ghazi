from products.forms import ProductForm
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterUsers


def index(request):
    return render(request, 'users/index.html')


def user_register(request):
    '''
    Create user account
    '''
    if request.method == 'POST':
        form = RegisterUsers(request.POST)
        if form.is_valid():
            data_username = form.cleaned_data['username']
            data_email = form.cleaned_data['email']
            data_password = form.cleaned_data['password']
            user = User.objects.create_user(data_username,
                                            data_email, data_password)
            user.save()
            return redirect('/')
    else:
        form = RegisterUsers()

    return render(request, 'users/register.html', {'form': form})


def login_user(request):
    '''
    Authenticate user and create session
    '''
    form = RegisterUsers(request.POST)
    if form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = authenticate(request, username=username,
                            email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            pass
    else:
        messages.error(request, "Error")
    return render(request, 'users/login.html', {'form': form})


def user_account(request):
    '''
    Displays user account details
    '''
    form_prod = ProductForm(request.POST)
    return render(request, 'users/user_account.html', {'form': form_prod})


def logout_user(request):
    '''
    User logout
    '''
    logout(request)
    return redirect('/')
