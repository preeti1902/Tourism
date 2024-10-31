from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import User
from packages.models import TravelPackage

class Booking(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(TravelPackage, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    number_of_people = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('confirmed', 'Confirmed'), ('pending', 'Pending'), ('cancelled', 'Cancelled')])

    def  __str__(self) -> str:
            return f'Booking details of user: {self.user.username} with destination: {self.package.destination.destination_name}'