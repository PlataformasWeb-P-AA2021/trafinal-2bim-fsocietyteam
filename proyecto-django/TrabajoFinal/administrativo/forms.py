from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Persona, \
        Barrio, Casa, Departamento

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ['nombres', 'apellidos', 'cedula', 'correo']
        labels = {
            'nombres': _('Ingrese sus nombres por favor'),
            'apellidos': _('Ingrese sus apellidos por favor'),
            'cedula': _('Ingrese cédula por favor'),
            'correo': _('Ingrese correo por favor'),
        }

class BarrioForm(ModelForm):
    class Meta:
        model = Barrio
        fields = ['nombreBarrio', 'siglas']
        labels = {
            'nombreBarrio': _('Ingrese el nombre del barrio'),
            'siglas': _('Ingrese las siglas del barrio'),
        }

class CasaForm(ModelForm):
    class Meta:
        model = Casa
        fields = ['propietario', 'direccion', 'barrio','valorCasa','colorCasa', 'numCuartos', 'numPisos']
        labels = {
            'propietario': _('Ingrese el nombre del propietario'),
            'direccion': _('Ingrese la direccion'),
            'valorCasa': _('Ingrese el valor de la casa'),
            'colorCasa': _('Ingrese el color de casa'),
            'numCuartos': _('Ingrese el numero de cuartos'),
            'numPisos': _('Ingrese el numero de pisos'),
        }


class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['propietario', 'direccion', 'barrio','valorDepartamento','numCuartos', 'valorMantenimiento']
        labels = {
            'propietario': _('Ingrese el nombre del propietario'),
            'direccion': _('Ingrese la direccion'),
            'valorDepartamento': _('Ingrese el valor del departamento'),
            'numCuartos': _('Ingrese el numero de cuartos'),
            'valorMantenimiento': _('Ingrese el valor del mantenimiento'),
        }

