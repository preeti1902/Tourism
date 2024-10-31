from django.db import models
from base.models import BaseModel
from django.utils.text import slugify
from django.contrib.auth.models import User

# Category class - for the different category like "Beach", "Mountain", "City", etc.
class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True,blank=True)
    description = models.TextField(blank=True, null=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args,**kwargs)

    def  __str__(self) -> str:
        return self.category_name
    
# Destination class - for the different destination along with there fields
class Destination(BaseModel):
    destination_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True,blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to="destinations")
    rating = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="catagories")
    price = models.IntegerField()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.destination_name)

        previous = Destination.objects.filter(uid=self.uid).first()
        image_changed = not previous or previous.image != self.image
        
        super(Destination, self).save(*args, **kwargs)

        if image_changed:
            ImageGallery.objects.update_or_create(
                destination=self,
                defaults={"image": self.image, "caption": f"Main image for {self.destination_name}"}
            )

    def __str__(self):
        return self.destination_name
    
# ImageGallery class to allow multiple images for a destination 
class ImageGallery(BaseModel):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name="gallery")
    image = models.ImageField(upload_to="destination_gallery")  
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.destination.destination_name}"

# Review class to add reviews to the destination by user's
class Review(BaseModel):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} on {self.destination.name}'