from django.contrib import admin

from .models import *

class Travelersinfo(admin.StackedInline):
    model = Travelers

class BookingTravelersinfo(admin.ModelAdmin):
    inlines = [Travelersinfo]

admin.site.register(Booking, BookingTravelersinfo)
admin.site.register(Coupon)
admin.site.register(Travelers)