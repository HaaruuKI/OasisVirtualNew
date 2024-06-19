from django.db import models

class Imagen(models.Model):
    nombre = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='imagenes/')
