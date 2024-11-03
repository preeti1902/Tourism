from django.shortcuts import render,get_object_or_404
from bookings.models import Booking,Coupon

def booking_page(request,uid):
    booking = get_object_or_404(Booking,uid=uid)
    coupons = Coupon.objects.all()
    context = {'booking': booking,'coupons':coupons}
    return render(request, 'bookings/booking_summary.html',context)
