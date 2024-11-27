from django.contrib import admin

from .models import *

admin.site.register(Room)

class TravelPackageImageAdmin(admin.StackedInline):
    model = ImageGallery

class TravelPackageAdmin(admin.ModelAdmin):
    inlines = [TravelPackageImageAdmin]

admin.site.register(TravelPackage, TravelPackageAdmin)
admin.site.register(ImageGallery)