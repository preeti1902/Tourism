from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import User
from destinations.models import Destination

class Review(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

