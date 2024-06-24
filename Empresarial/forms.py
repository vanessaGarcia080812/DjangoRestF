
from django import forms   # type: ignore 
from .models import Empleado,Empresa, Calculos, Novedades

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields ='__all__'
        
        
        # ['numero_identificacion', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'estado_civil']

    # def __init__(self, *args, **kwargs):
    #     super(EmpleadoForm, self).__init__(*args, **kwargs)
    #     readonly_fields = ['numero_identificacion', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido']
    #     for filtro in self.fields:
    #         if filtro in readonly_fields:
    #             self.fields[filtro].widget.attrs['readonly'] = True

class LoginForm(forms.Form):
    numero_identificacion = forms.IntegerField(label='Número de identificación')
    contrasena = forms.CharField(label='Contraseña', widget=forms.PasswordInput)


class RecuperarContrasenaForm(forms.Form):
    numero_identificacion = forms.IntegerField(label='Número de Identificación')


class PasswordResetForm(forms.Form):
    token = forms.CharField(label='Token', max_length=255)
    new_password = forms.CharField(label='Nueva Contraseña', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    

class NovedadesForm(forms.ModelForm):
    class Meta:
        model = Novedades
        fields = [
            'HorasExDiu',
            'HorasExNoc',
            'HorasExFestivaNoc',
            'HorasExFestivaDiu',
            'recargoDiuFes',
            'recargoNoc',
            'recargoNocFest',
        ]

    def clean(self):
        cleaned_data = super().clean()
        
        # Definir una función para obtener el valor del campo o devolver 0 si es None o vacío
        def get_valor_campo(campo):
            valor = cleaned_data.get(campo)
            return valor if valor is not None and valor != '' else 0
        
        # Obtener los valores de los campos y manejar valores vacíos o None
        horas_ex_diu = get_valor_campo('HorasExDiu')
        horas_ex_noc = get_valor_campo('HorasExNoc')
        horas_ex_festiva_noc = get_valor_campo('HorasExFestivaNoc')
        horas_ex_festiva_diu = get_valor_campo('HorasExFestivaDiu')
        recargo_diu_fes = get_valor_campo('recargoDiuFes')
        recargo_noc = get_valor_campo('recargoNoc')
        recargo_noc_fest = get_valor_campo('recargoNocFest')

        # Calcular la suma total de horas
        horas_totales = (
            horas_ex_diu + horas_ex_noc +
            horas_ex_festiva_noc + horas_ex_festiva_diu
        )

        # Validar si la suma total de horas excede 48
        if horas_totales > 48:
            raise forms.ValidationError('La suma de horas no puede exceder 48.')

        return cleaned_data