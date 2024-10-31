from django.shortcuts import render

def review_page(request):
    return render(request, 'reviews/review.html')
