from django.shortcuts import redirect,render
from destinations.models import Destination
from bookings.models import Booking
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def destinations(request):
    context = {'destinations':Destination.objects.all()}
    return render(request, 'destination/destinations.html',context)

def get_destination(request, slug):
    try:
        destination = Destination.objects.get(slug=slug)
        if request.method == 'POST':
            from_date = request.POST.get('from-date')
            to_date = request.POST.get('to-date')
            guests = int(request.POST.get('guests'))
            
            tax_amount = (destination.price * guests) * 0.18  
            total_price = (destination.price * guests) + tax_amount 

            booking = Booking.objects.create(
                user=request.user,
                destination=destination,
                start_date=from_date,
                end_date=to_date,
                number_of_people=guests,
                total_price=total_price,
                booking_date=timezone.now(),
                status='pending'
            )
            return HttpResponseRedirect(reverse('booking_page', args=[booking.uid]))
        else:
            return render(request,'destination/destination.html',context = {'destination':destination})
    except Exception as e:
        print(e)
