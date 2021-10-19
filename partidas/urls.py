from django.urls import path


from .views import (
    PartidaCreateView,
    PartidaDetailView,
    PartidaEnCanchaCreateView,
    solicitud_create_view,
    solicitud_accept_view,
    solicitud_reject_view,
)

urlpatterns = [
    path('<int:pk>/', PartidaDetailView.as_view(), name="detail_partida"),
    path('crear/', PartidaCreateView.as_view(), name="crear_partida"),
    path('crear/<int:cancha>/', PartidaEnCanchaCreateView.as_view(),
         name="crear_partida_en_cancha"),
    path('crear/solicitud/<int:partida_id>',
         solicitud_create_view, name="crear_solicitud"),
    path('accept/solicitud/<int:pk>/',
         solicitud_accept_view, name="accept_solicitud"),
    path('reject/solicitud/<int:pk>/',
         solicitud_reject_view, name="reject_solicitud"),
]
