from django.shortcuts import render
from destinations.models import Destination

def load_destinations(request):
    context = {'destinations':Destination.objects.all()}
    return render(request, 'destination/destinations.html',context)