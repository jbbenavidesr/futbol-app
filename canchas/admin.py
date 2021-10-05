from django.contrib import admin

from canchas.models import Cancha


class CanchaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "direccion", "telefono", "precio")


admin.site.register(Cancha, CanchaAdmin)
