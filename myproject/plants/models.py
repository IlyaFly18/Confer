from django.db import models
from beds.models import Bed


class Plant(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField(default=None)
    bed = models.ForeignKey(Bed, on_delete=models.CASCADE, null=True)
    x = models.CharField(max_length=30)
    y = models.CharField(max_length=30)
    date = models.DateField(default=None)


class PlantFunction(models.Model):
    name = models.TextField()
    first_date = models.DateField()
    period = models.IntegerField()
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, null=True)

