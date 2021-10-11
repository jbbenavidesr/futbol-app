from django.urls import path

from .views import PartidaCreateView

urlpatterns = [
    path('crear/', PartidaCreateView.as_view(), name="crear_partida"),
]
