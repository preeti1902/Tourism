from django.shortcuts import render,get_object_or_404
from bookings.models import Booking,Coupon,Travelers
from django.http import JsonResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib import messages



def booking_page(request, uid):
    booking = get_object_or_404(Booking, uid=uid)
    coupons = Coupon.objects.all()

    if request.method == "POST":
        promo_code = request.POST.get("promo_code")
        selected_coupon = Coupon.objects.filter(coupon_code=promo_code).first()

        if selected_coupon and booking.total_price >= selected_coupon.minimum_amount:
            booking.coupon = selected_coupon
            booking.save()
            messages.success(request, "Coupon applied successfully")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.warning(request,'Coupon not applicable')
            return HttpResponseRedirect(request.path_info)

    context = {'booking': booking, 'coupons': coupons}
    return render(request, 'bookings/booking_summary.html', context)

@csrf_exempt
def submit_booking_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        try:
            booking = Booking.objects.get(uid=data['booking_id'])
        except Booking.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Booking not found.'})
        
        booking.user.email = data['email']
        booking.user.mobile_number = data['mobile']  # Assuming a mobile field in User model
        booking.user.save()
        
        for traveler in data['travelers']:
            Travelers.objects.create(
                booking=booking,
                gender=traveler['gender'],
                first_name=traveler['first_name'],
                last_name=traveler['last_name']
            )
        
        return JsonResponse({'success': True})
    
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})