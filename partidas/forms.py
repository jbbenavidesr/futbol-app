from django import forms
from django.contrib.admin import widgets

from .models import Partida


class PartidaCreateForm(forms.ModelForm):
    cuando = forms.SplitDateTimeField(widget=widgets.AdminSplitDateTime)

    class Meta:
        model = Partida
        exclude = ('creado_por',)


class PartidaEnCanchaCreateForm(forms.ModelForm):
    cuando = forms.SplitDateTimeField(widget=widgets.AdminSplitDateTime)

    class Meta:
        model = Partida
        exclude = ('creado_por', 'cancha')
