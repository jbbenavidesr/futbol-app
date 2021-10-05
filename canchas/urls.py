from django.urls import path
from .views import CanchasListView, CanchasDetailView

urlpatterns = [
    path('', CanchasListView.as_view(), name="lista_canchas"),
    path('<int:pk>/', CanchasDetailView.as_view(), name="detalle_cancha"),
]
