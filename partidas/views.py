from django.http.response import HttpResponseRedirect
from django.views.generic import DetailView
from django.views.generic.edit import CreateView

from .models import Partida
from .forms import PartidaCreateForm


class PartidaDetailView(DetailView):
    model = Partida
    template_name = "partidas/partida_detail.html"
    context_object_name = "partida"


class PartidaCreateView(CreateView):
    model = Partida
    form_class = PartidaCreateForm
    template_name = "partidas/crear.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creado_por = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
