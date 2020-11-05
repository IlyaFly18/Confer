from django.db import models

class RainPeriod(models.Model):
    city = models.CharField(max_length=30)
    date = models.DateTimeField()
    description_weather = models.CharField(max_length=30)

    def __str__(self):
        return self.city
