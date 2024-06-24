
from django import forms   # type: ignore 
from .models import Independiente, DatosCalculos


class IndependienteForm(forms.ModelForm):
    class Meta:
        model = Independiente
        fields ='__all__'


class DatosCalculosForm(forms.ModelForm):
    class Meta:
        model = DatosCalculos
        fields = ['salarioBase', 'ibc', 'salud', 'pension', 'arl', 'CCF']