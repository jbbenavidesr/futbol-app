from django.urls import path

from .views import PartidaCreateView, PartidaDetailView

urlpatterns = [
    path('<int:pk>/', PartidaDetailView.as_view(), name="detail_partida"),
    path('crear/', PartidaCreateView.as_view(), name="crear_partida"),
]
