from django.db import models

class ZipCode(models.Model):
    value = models.IntegerField()

class HousingUnits(models.Model):
	zipcode_id = models.IntegerField(default=0)
	total = models.IntegerField(default=0)
	occupied = models.IntegerField(default=0)
	vacant = models.IntegerField(default=0)