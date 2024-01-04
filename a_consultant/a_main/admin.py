from django.contrib import admin
from .models import *

admin.site.register(Car)
admin.site.register(Brand)
admin.site.register(TripBooking)
admin.site.register(Bookmark)
admin.site.register(CarRental)