from django.urls import path 
from packages.views import package_page,get_package

urlpatterns = [
    path('package/',package_page,name="package_page"),
    path('<slug>/',get_package,name='get_package')
]