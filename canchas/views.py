from django.views.generic import ListView, DetailView
from .models import Cancha


class CanchasListView(ListView):
    model = Cancha
    template_name = "home.html"
    context_object_name = "lista_canchas"


class CanchasDetailView(DetailView):
    model = Cancha
    template_name = "canchas/cancha_detail.html"
    context_object_name = "cancha"
