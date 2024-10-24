from django.contrib import admin
from django.urls import path
from accounts.views import login_page,register_page,forgot_Password_page,reset_password_page,logging_out,activate_email

urlpatterns = [
    path('login/',login_page,name="login"),
    path('register/', register_page, name="register"),
    path('forget-password/', forgot_Password_page, name="forget-password"),
    path('password-reset/<token>/', reset_password_page, name="password-reset"),
    path('logout/', logging_out, name='logout'),
    path('activate/<email_token>/',activate_email, name="activate_email"),

]
