from django.contrib import admin

from .models import *
from .templatetags.range_tags import *

admin.site.register(Category)
admin.site.register(Destination)
admin.site.register(Review)
admin.site.register(ImageGallery)