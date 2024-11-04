from django.urls import path 
from bookings.views import booking_page,submit_booking_data

urlpatterns = [
    path('bookings/<uid>/',booking_page,name="booking_page"),
    path('submit-booking-data/', submit_booking_data, name='submit_booking_data'),
]