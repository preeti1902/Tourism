from django.db import models
from base.models import BaseModel
from destinations.models import Destination

class Room(BaseModel):
    room_name = models.CharField(max_length=50)
    cost = models.IntegerField()
    accommodation = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.room_name}"

class TravelPackage(BaseModel):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(help_text='Duration in days')
    itinerary = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE,null=True)
    available_from = models.DateField()
    available_to = models.DateField()
    image = models.ImageField(upload_to='packages/')

    def  __str__(self) -> str:
        return f'Travel Package of {self.destination.destination_name}'
