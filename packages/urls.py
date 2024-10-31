from django.urls import path 
from packages.views import package_page

urlpatterns = [
    path('packages/',package_page,name="package_page")
]