from django.shortcuts import render
import requests

def login_page(request):
    return render(request, 'accounts/login.html')