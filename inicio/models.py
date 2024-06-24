from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=255)
    developer = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    release_date = models.DateField()
    genre = models.CharField(max_length=255)
    platforms = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField()
