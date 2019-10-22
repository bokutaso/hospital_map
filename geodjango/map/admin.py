#from django.contrib import admin
from django.contrib.gis import admin
from map.models import Border
from leaflet.admin import LeafletGeoAdmin

class BorderAdmin(LeafletGeoAdmin):
  search_fields = ['n03_001','n03_003','n03_004']
  list_filter = ('n03_003')

admin.site.register(Border, admin.OSMGeoAdmin)
#admin.site.register(School, admin.GeoModelAdmin)
#admin.site.register(Facility, admin.GeoModelAdmin)
#admin.site.register(Busstop, admin.GeoModelAdmin)

# Register your models here.
