import random

from django.db import models
from django.urls import reverse

IMAGE_CHOICES = (
    ('images/cancha1.jpeg', "Cancha 1"),
    ('images/cancha2.jpeg', "Cancha 2"),
    ('images/cancha3.jpeg', "Cancha 3"),
    ('images/cancha4.jpeg', "Cancha 4"),
    ('images/cancha5.jpeg', "Cancha 5"),
    ('images/cancha6.jpeg', "Cancha 6"),
    ('images/cancha7.jpeg', "Cancha 7"),
)


class Cancha(models.Model):
    """
    Modelo que describe una cancha.
    """
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.BigIntegerField()
    precio = models.IntegerField()
    descripcion = models.TextField("")
    image = models.CharField(
        max_length=20, choices=IMAGE_CHOICES, default='images/cancha1.jpeg')

    # Missing Image

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('detalle_cancha', args=[str(self.id)])

    def rating(self):
        return range(random.randint(1, 5))
