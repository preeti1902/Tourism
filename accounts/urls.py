from django.contrib import admin
from django.urls import path
from accounts.views import login_page

urlpatterns = [
    path('user/',login_page,name="login_signup")
]

# Yet to fix the url