import random

from django.db import models
from django.urls import reverse


class Cancha(models.Model):
    """
    Modelo que describe una cancha.
    """
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.BigIntegerField()
    precio = models.IntegerField()
    descripcion = models.TextField("")

    # Missing Image

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('detalle_cancha', args=[str(self.id)])

    def rating(self):
        return range(random.randint(0, 5))
