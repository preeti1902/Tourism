from django.shortcuts import render

def package_page(request):
    return render(request, 'packages/package.html')
