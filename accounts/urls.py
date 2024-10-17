from django.contrib import admin
from django.urls import path
from accounts.views import login,register,forgot_Password

urlpatterns = [
    path('login/',login,name="login"),
    path('register/', register, name="register"),
    path('reset/', forgot_Password, name="resetPassword")

]
