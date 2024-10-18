from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful.')
            return redirect('accounts:login')
        else:
            messages.error(request, 'Registration failed.')
    else:
        form = RegisterForm()
    
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('pages:index')
                else:
                    messages.info(request, 'Your account is not active.')
            else:
                messages.info(request, 'Invalid login credentials.')
    else:
        form = LoginForm()
    
    context = {
        'form': form
    }
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('pages:index')

@login_required(login_url='accounts:login')
def dashboard_view(request):
    current_user = request.user
    context = {
        'current_user': current_user
    }
    return render(request, 'dashboard.html', context)