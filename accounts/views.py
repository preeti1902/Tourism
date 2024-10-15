from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

def login_page(request):
    return render(request, 'accounts/login_signup.html')

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        user_obj = User.objects.filter(username = email)
    
        if user_obj.exists():
            messages.warning(request, 'Email is already taken.')
            return HttpResponseRedirect(request.path_info)

        user_obj = User.objects.create(email = email , password= password , confirm_password = confirm_password , username = email)
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, 'An email has been sent on your mail.')
        return HttpResponseRedirect(request.path_info)

    return render(request, 'accounts/login_signup.html')