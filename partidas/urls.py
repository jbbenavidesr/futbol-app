from django.urls import path


from .views import PartidaCreateView, PartidaDetailView, PartidaEnCanchaCreateView, solicitud_create_view

urlpatterns = [
    path('<int:pk>/', PartidaDetailView.as_view(), name="detail_partida"),
    path('crear/', PartidaCreateView.as_view(), name="crear_partida"),
    path('crear/<int:cancha>/', PartidaEnCanchaCreateView.as_view(),
         name="crear_partida_en_cancha"),
    path('crear/solicitud/<int:partida_id>',
         solicitud_create_view, name="crear_solicitud"),
]
