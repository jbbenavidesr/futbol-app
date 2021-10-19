from django.http.response import HttpResponseRedirect
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from canchas.models import Cancha

from .models import Partida, Solicitud
from .forms import PartidaCreateForm, PartidaEnCanchaCreateForm


class PartidaDetailView(DetailView):
    model = Partida
    template_name = "partidas/partida_detail.html"
    context_object_name = "partida"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['solicitado'] = False

        solicitudes = user.solicitudes.all()
        for solicitud in solicitudes:
            partida = solicitud.partida
            if partida.id == self.kwargs['pk']:
                context['solicitado'] = True

        return context


class PartidaCreateView(LoginRequiredMixin, CreateView):
    form_class = PartidaCreateForm
    template_name = "partidas/crear.html"
    login_url = 'login'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creado_por = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class PartidaEnCanchaCreateView(LoginRequiredMixin, CreateView):
    form_class = PartidaEnCanchaCreateForm
    template_name = "partidas/crear.html"
    login_url = 'login'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creado_por = self.request.user
        cancha = Cancha.objects.get(id=self.kwargs['cancha'])
        self.object.cancha = cancha
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


@login_required
def solicitud_create_view(request, partida_id):
    user = request.user
    partida = Partida.objects.get(pk=partida_id)
    sol = Solicitud.objects.create(partida=partida, usuario=user)

    return redirect(partida)
