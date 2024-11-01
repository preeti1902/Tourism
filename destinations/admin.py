from django.contrib import admin

from .models import *
from .templatetags.range_tags import *

admin.site.register(Category)
admin.site.register(Review)

class DestinationImageAdmin(admin.StackedInline):
    model = ImageGallery

class DestinationAdmin(admin.ModelAdmin):
    inlines = [DestinationImageAdmin]

admin.site.register(Destination, DestinationAdmin)
admin.site.register(ImageGallery)
