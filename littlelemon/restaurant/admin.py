# admin.py in the restaurant app package folder

from django.contrib import admin
from .models import Menu, Booking

admin.site.register(Menu)
admin.site.register(Booking)
