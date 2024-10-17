from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def login_view(request):
    return render(request, 'login.html')

def logout_view(request):
    return render(request, 'register.html')

def register_view(request):
    return render(request, 'register.html')

def dashboard_view(request):
    pass