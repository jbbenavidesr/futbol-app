from django import forms
from django.contrib.admin import widgets

from .models import Partida


class PartidaCreateForm(forms.ModelForm):

    class Meta:
        model = Partida
        exclude = ('creado_por',)

    def __init__(self, *args, **kwargs):
        super(PartidaCreateForm, self).__init__(*args, **kwargs)
        self.fields['cuando'].widget = widgets.AdminSplitDateTime()
