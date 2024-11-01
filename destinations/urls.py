from django.urls import path 
from destinations.views import destinations,get_destination

urlpatterns = [
    path('destinations/',destinations,name="load_destinations"),
    path('<slug>/',get_destination,name='get_destination')
]