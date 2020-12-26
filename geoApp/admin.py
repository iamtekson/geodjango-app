from django.contrib import admin
from .models import Location
from leaflet.admin import LeafletGeoAdmin


admin.site.register(Location, LeafletGeoAdmin)
