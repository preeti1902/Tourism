from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from accounts.models import *
from accounts.emails import send_password_reset_email

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

def forgot_Password_page(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            print(email)
            if not User.objects.filter(email=email).first():
                messages.error(request, 'User Not Found')
                return redirect('/forgot-password-page')
            user_obj = User.objects.get(email=email)
            token = str(uuid.uuid4())
            profile_obj = Profile.objects.get(user = user_obj)
            profile_obj.forget_password_token = token
            profile_obj.save()
            send_password_reset_email(user_obj,token)
            messages.warning(request, 'Reset Password Link has been sent to your email')
            return redirect('forget-password')
    except Exception as e:
        print(e)
    return render(request, 'accounts/forgot_password_page.html')


def reset_password_page(request, token):
    context = {}
    try:
        profile_obj = Profile.objects.get(forget_password_token=token)
        context = {'user_id': profile_obj.user.id}

        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            user_id = request.POST.get('user_id')

            if not user_id:
                messages.warning(request, 'No user id found')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            if new_password != confirm_password:
                messages.error(request, 'Passwords do not match')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
            user_obj = User.objects.get(id=user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            
            messages.success(request, 'Password was changed successfully')
            return redirect('login')

    except Profile.DoesNotExist:
        messages.error(request, 'Invalid or expired token')

    return render(request, 'accounts/reset_password_page.html', context)
    
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