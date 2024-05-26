from django.contrib.gis.db import models

class VillageMap(models.Model):
    survey_no = models.CharField(max_length=50)
    geom = models.MultiPolygonField()
