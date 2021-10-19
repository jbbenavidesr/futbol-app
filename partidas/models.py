from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

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

    def get_absolute_url(self):
        return reverse('detail_partida', args=[str(self.id)])


class Solicitud(models.Model):
    partida = models.ForeignKey(
        Partida,
        on_delete=models.CASCADE,
        related_name='solicitudes'
    )

    usuario = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='solicitudes',
    )

    is_accepted = models.BooleanField(blank=True, null=True)

    class Meta:
        unique_together = ('partida', 'usuario',)
