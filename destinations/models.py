from django.db import models
from base.models import BaseModel
from django.utils.text import slugify

# Category class - for the different category like "Beach", "Mountain", "City", etc.
class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    category_img = models.ImageField(upload_to="catagories")
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
    rating = models.FloatField(default=0.0)
    popular = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="catagories")
    price = models.IntegerField()
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(Destination,self).save(*args,**kwargs)

    def __str__(self) -> str:
        return self.name
    
# ImageGallery class to allow multiple images for a destination 
class ImageGallery(BaseModel):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name="gallery")
    image = models.ImageField(upload_to="destination_gallery")
    caption = models.CharField(max_length=255, blank=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.destination.destination_name)

# Review class to add reviews to the destination by user's
class Review(BaseModel):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='reviews')
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f'Review by {self.user.username} on {self.destination.name}'