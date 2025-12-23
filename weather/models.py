from django.db import models

class WeatherRecord(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.FloatField()
    rain = models.FloatField(default=0)
    description = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} at {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
