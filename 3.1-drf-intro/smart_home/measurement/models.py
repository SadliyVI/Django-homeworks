from django.utils import timezone
from django.db import models



class Sensor(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE,
                               related_name="measurements",
                               verbose_name="ID датчика")
    temperature = models.FloatField(verbose_name="Температура при измерении")
    measured_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата ")


    def __str__(self):
        return f"{self.temperature}°C @ {self.measured_at}"

