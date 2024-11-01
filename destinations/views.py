from django.shortcuts import render
from destinations.models import Destination

def destinations(request):
    context = {'destinations':Destination.objects.all()}
    return render(request, 'destination/destinations.html',context)

def get_destination(request, slug):
    context = {'destination': Destination}
    return render(request,'destination/destination.html',context)