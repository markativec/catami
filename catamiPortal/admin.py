from django.contrib.gis import admin
from models import Force

admin.site.register(Force, admin.OSMGeoAdmin)
