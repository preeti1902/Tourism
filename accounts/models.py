from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100, null=True, blank=True)
    forget_password_token = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"Profile for {self.user.username}"
    
class ProfileImage(BaseModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile_images")
    image = models.ImageField(upload_to='profile')

    def __str__(self):
        return f"Profile Image of {self.profile.user.username}"
    
