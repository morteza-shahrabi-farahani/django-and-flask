from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from listings.models import Listing
from realtors.models import Realtor 
from listings.choices import state_choices, bedroom_choices, price_choices
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        return  
    else:             
        return render(request, 'accounts/login.html')

def logout(request):
    return redirect('index')

def register(request):
    if request.method == 'POST':
        messages.error(request, 'Testing error message')
        return redirect('register')  
    else: 
        return render(request, 'accounts/register.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')