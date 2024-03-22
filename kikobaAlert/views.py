from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.

def about_view(request):
    """ This function is responsible for rendering the about page.
    The function will contain informations about kikobaAlert as Application
    and other information about the application"""
    return render(request, 'kikobaAlert/about.html',{})

def admin_dashboard_view(request):
    """This function is for rendering the admin dashboard view.
    where will contains logics for admin dashboard in kikobaAlert Application"""
    
    return render(request , 'kikobaAlert/admin_dashboard.html',{})


def customer_dashboard_view(request):
    """customer_dashboard_view is responsible for rendering the customer dashboard.
    This function will contain informations about customer dashboard in kikobaAlert"""
    
    return render(request, 'kikobaAlert/customer_dashboard.html',{})


def login_view(request):
    """login_view function will contains logics for login in kikobaAlert
    The function is responsible for for authenticate the customers credentials,
    Before allowed login in customer dashboard"""
    
    form = forms.LoginForm()
    return render(request, 'kikobaAlert/login.html',{'form':form})

def register_view(request):
    """register_view responsible for registering customers in kikobaAlert Application
    This function will be working for validating primary credentials entered from kikobaAlert Registration form,
    like password and confirmed password if they match!. as well checking for existence of email address provided by the customer
    since only one email address is required for registration to work correctly and already registered email address,
    will not be used to register another customer"""
    form = forms.RegistrationForm()
    return render (request, 'kikobaAlert/register.html',{'form': form})
