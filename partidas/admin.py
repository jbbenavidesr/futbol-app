from django.contrib import admin

from .models import Partida, Solicitud


class SolicitudInline(admin.TabularInline):
    model = Solicitud


class PartidaAdmin(admin.ModelAdmin):
    inlines = [
        SolicitudInline,
    ]
    list_display = ("cancha", "cuando", "cupos", "creado_por")


admin.site.register(Partida)
