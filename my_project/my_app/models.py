from django.db import models

# Create your models here.
class SensorData(models.Model):
    humidity = models.FloatField()
    temperature = models.FloatField()
    time = models.DateTimeField()
