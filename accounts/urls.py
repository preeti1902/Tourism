from django.contrib import admin
from django.urls import path
from accounts.views import login_page,register_page,forgot_Password,send_email_link,logging_out,activate_email

urlpatterns = [
    path('login/',login_page,name="login"),
    path('register/', register_page, name="register"),
    path('reset/', forgot_Password, name="resetPassword"),
    path('password/', send_email_link, name="email_Link"),
    path('logout/', logging_out, name='logout'),
    path('activate/<email_token>/',activate_email, name="activate_email"),

]
