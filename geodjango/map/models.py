from django.contrib.gis.db import models

class Border(models.Model):
    n03_001 = models.CharField(max_length=50)
    n03_002 = models.CharField(max_length=50)
    n03_003 = models.CharField(max_length=50)
    n03_004 = models.CharField(max_length=50)
    n03_007 = models.CharField(max_length=50)
    geom = models.PolygonField(srid=4326)

    def __str__(self):
        return self.n03_004