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



class PropietarioCasaForm(ModelForm):

    def _init_(self, Persona, *args, **kwargs):
        super(PropietarioCasaForm, self)._init_(*args, **kwargs)
        self.initial['persona'] = persona
        self.fields["persona"].widget = forms.widgets.HiddenInput()
        print(persona)

    class Meta:
        model = Casa
        fields = ['propietario', 'direccion', 'barrio','valorCasa','colorCasa', 'numCuartos', 'numPisos']


class BarrioCasaForm(ModelForm):

    def _init_(self, Barrio, *args, **kwargs):
        super(BarrioCasaForm, self)._init_(*args, **kwargs)
        self.initial['barrio'] = barrio
        self.fields["barrio"].widget = forms.widgets.HiddenInput()
        print(barrio)

    class Meta:
        model = Casa
        fields = ['propietario', 'direccion', 'barrio','valorCasa','colorCasa', 'numCuartos', 'numPisos']


class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['propietario', 'direccion', 'barrio','valorDepartamento','numCuartos', 'valorMantenimiento']

class PropietarioDepartamentoForm(ModelForm):

    def _init_(self, Persona, *args, **kwargs):
        super(PropietarioCasaForm, self)._init_(*args, **kwargs)
        self.initial['persona'] = persona
        self.fields["persona"].widget = forms.widgets.HiddenInput()
        print(persona)

    class Meta:
        model = Departamento
        fields = ['propietario', 'direccion', 'barrio','valorDepartamento','numCuartos', 'valorMantenimiento']


class BarrioDepartamentoForm(ModelForm):

    def _init_(self, Barrio, *args, **kwargs):
        super(BarrioCasaForm, self)._init_(*args, **kwargs)
        self.initial['barrio'] = barrio
        self.fields["barrio"].widget = forms.widgets.HiddenInput()
        print(barrio)

    class Meta:
        model = Departamento
        fields = ['propietario', 'direccion', 'barrio','valorDepartamento','numCuartos', 'valorMantenimiento']