from django.db import models
from base.models import BaseModel
from destinations.models import Destination

# Create your models here.
class TravelPackage(BaseModel):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(help_text='Duration in days')
    itinerary = models.TextField()
    available_from = models.DateField()
    available_to = models.DateField()
    image = models.ImageField(upload_to='packages/')

    def  __str__(self) -> str:
        return f'Travel Package of {self.destination.destination_name}'
