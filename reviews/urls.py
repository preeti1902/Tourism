from django.urls import path 
from reviews.views import review_page

urlpatterns = [
    path('reviews/',review_page,name="review_page")
]