from django.shortcuts import render
from destinations.models import Destination

def destinations(request):
    context = {'destinations':Destination.objects.all()}
    return render(request, 'destination/destinations.html',context)

def get_destination(request, slug):
    try:
        destination = Destination.objects.get(slug=slug)
        return render(request,'destination/destination.html',context = {'destination':destination})
    except Exception as e:
        print(e)
