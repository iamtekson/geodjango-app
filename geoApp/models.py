from django.db import models
from django.contrib.gis.db import models as gis_modals


class Location(models.Model):
    name = models.CharField(max_length=100)
    location = gis_modals.PointField()

    def __str__(self):
        return self.name
