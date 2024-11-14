from django.shortcuts import redirect, render
from packages.models import TravelPackage
from bookings.models import Booking
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def  package_page(request):
    print("Rendering package page") 
    context = {'packages': TravelPackage.objects.all()}
    return render(request, 'packages/packages_page.html', context)

def get_package(request, slug):
    try:
        package = TravelPackage.objects.get(slug=slug)
        return render(request, 'packages/package_detail.html', {'package': package})
    except TravelPackage.DoesNotExist:
        return HttpResponse('Package not found', status=404)
    