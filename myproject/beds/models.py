from django.db import models
from django.conf import settings

class Bed(models.Model):
    SHAPE_CHOICES = (
        ('1', 'Прямоугольная'),
        ('2', 'Круглая')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    shape = models.CharField(choices=SHAPE_CHOICES, max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Beds'
