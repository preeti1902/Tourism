from django.shortcuts import render

def load_destinations(request):
    return render(request, 'destination/destinations.html')