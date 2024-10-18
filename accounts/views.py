from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.filter(username=email)

        if not user.exists():
            messages.warning(request, "Account not found")
            return HttpResponseRedirect(request.path_info)
        
        user = user[0]

        user = authenticate(username=email, password=password)

        if user:
                login(request, user)
                return HttpResponseRedirect('/')
        messages.warning(request, "Invalid Credentials")
        return HttpResponseRedirect(request.path_info)
    return render(request, 'accounts/login_signup.html')

def register_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        user = User.objects.filter(username = email)

        if user.exists():
            messages.warning(request, 'Email is already taken.')
            return HttpResponseRedirect(request.path_info)

        print(email)

        user = User.objects.create_user(username=email, email=email)
        user.set_password(password)
        user.save()

        messages.success(request, 'Registration successful. You can now log in.')
        return HttpResponseRedirect('login')

    return render(request, 'accounts/login_signup.html')

def forgot_Password(request):
    return render(request, 'accounts/forgotpassword.html')


def send_email_link(request):
    return render(request, 'accounts/email.html')
    

    
