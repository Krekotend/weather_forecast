from django.db import models

class UserSearchHistory(models.Model):
    session_key = models.CharField(max_length=40)
    last_city = models.CharField(max_length=100)
    count = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('session_key', 'last_city')

class CitySearchCount(models.Model):
    city = models.CharField(max_length=100, unique=True)
    count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.city} - {self.count}"
