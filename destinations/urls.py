from django.urls import path 
from destinations.views import load_destinations

urlpatterns = [
    path('destinations/',load_destinations,name="load_destinations")
]