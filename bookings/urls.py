from django.urls import path 
from bookings.views import booking_page

urlpatterns = [
    path('bookings/<uid>/',booking_page,name="booking_page")
]