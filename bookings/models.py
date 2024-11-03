from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import User
from packages.models import TravelPackage
from destinations.models import Destination
from django.utils.text import slugify
from datetime import timedelta

class Coupon(BaseModel):
    coupon_code = models.CharField(max_length=10)
    is_expired = models.BooleanField(default=False)
    coupon_description = models.TextField(null=True)
    discount_price = models.IntegerField(default = 100)
    minimum_amount = models.IntegerField(default=500)
    def __str__(self) -> str:
        return self.coupon_code

class Booking(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE,related_name='destination', null=True)
    package = models.ForeignKey(TravelPackage, on_delete=models.CASCADE,related_name='package',null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    number_of_people = models.IntegerField()
    total_price = models.FloatField()
    booking_date = models.DateTimeField(auto_now_add=True)
    coupon = models.ForeignKey(Coupon,on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=50, choices=[('confirmed', 'Confirmed'), ('pending', 'Pending'), ('cancelled', 'Cancelled')])

    def get_total_duration(self):
        duration = self.end_date - self.start_date
        days = duration.days
        nights = max(0, days - 1) 
        return f"{days} days and {nights} nights"

    def get_cancel_date(self):
        return self.start_date - timedelta(days=1)
    
    def get_cancel_fee(self):
         return self.total_price*0.95

    def get_reschedule_fee(self):
         return self.total_price*0.70
    
    def total_tax_amount(self):
        total_tax_amount = (self.destination.price*self.number_of_people) * 0.18 
        return total_tax_amount
    
    def total_base_price(self):
        total_base_price = (self.destination.price*self.number_of_people)
        return total_base_price

    def  __str__(self) -> str:
            return f'Booking details of user: {self.user.username} with destination: {self.destination.destination_name}'
    
