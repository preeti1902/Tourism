from django.db import models
from base.models import BaseModel
from django.utils.text import slugify
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
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(help_text='Duration in days')
    itinerary = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE,null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super(TravelPackage,self).save(*args, **kwargs)

    def  __str__(self) -> str:
        return f'Travel Package of {self.destination.destination_name}'

class ImageGallery(BaseModel):
    destination = models.ForeignKey(TravelPackage, on_delete=models.CASCADE, related_name="gallery")
    image = models.ImageField(upload_to="TravelPackage_gallery")  

    def __str__(self):
        return f"Image for {self.destination.destination_name}"