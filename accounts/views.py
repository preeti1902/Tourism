from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from accounts.models import *

def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username=email)

        user = user_obj[0]
        
        if not user_obj[0].profile.is_email_verified:
            messages.warning(request, 'Your account is not verified.')
            return HttpResponseRedirect(request.path_info)
        
        if user.profile.is_email_verified:
            # User is already verified, proceed with login
            user_obj = authenticate(username=email, password=password)

            if user_obj:
                login(request, user_obj)
                return HttpResponseRedirect('/')
            
            messages.warning(request, "Invalid Credentials")
            return HttpResponseRedirect(request.path_info)
        else:
            # User email is not verified, initiate activation
            email_token = str(uuid.uuid4())
            profile = Profile.objects.create(user=user, email_token=email_token)
            send_account_activation_email(email, email_token)

            messages.warning(request, 'Please verify your email before logging in. Activation email sent.')
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
        return HttpResponseRedirect(request.path_info)

    return render(request, 'accounts/login_signup.html')

def forgot_Password(request):
    return render(request, 'accounts/forgotpassword.html')


def send_email_link(request):
    return render(request, 'accounts/email.html')
    
def logging_out(request):
    logout(request)
    return redirect('/')
    
def activate_email(request, email_token):
    try:
        user = Profile.objects.get(email_token=email_token)
        user.is_email_verified = True
        user.save()
        messages.success(request, 'Email Is Verified, Please Login')
        return redirect('/')
    except Profile.DoesNotExist:
        print(f'Invalid Email Token: {email_token}')
        return HttpResponse('Invalid Email Token')