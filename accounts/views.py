from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request)
            messages.success(request, 'You are logged in!')
            return HttpResponseRedirect(request.path_info)  
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'accounts/login_signup.html')

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return HttpResponseRedirect(request.path_info)

        if User.objects.filter(username=email).exists():
            messages.warning(request, 'Email is already taken.')
            return HttpResponseRedirect(request.path_info)

        user_obj = User.objects.create_user(username=email, email=email, password=password)
        user_obj.save()

        messages.success(request, 'Registration successful. You can now log in.')
        return HttpResponseRedirect(request.path_info)

    return render(request, 'accounts/login_signup.html')

def forgot_Password(request):
    return render(request, 'accounts/forgotpassword.html')
    
