from django.db import models
from django.contrib.auth import get_user_model

from canchas.models import Cancha


class Partida(models.Model):
    cuando = models.DateTimeField()
    mensaje = models.CharField(max_length=255)
    cupos = models.IntegerField()
    cancha = models.ForeignKey(
        Cancha,
        on_delete=models.CASCADE,
        related_name='partidas',
    )
    creado_por = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='partidas'
    )

    def __str__(self):
        return f"Partida {self.id} en {self.cancha.nombre}"
