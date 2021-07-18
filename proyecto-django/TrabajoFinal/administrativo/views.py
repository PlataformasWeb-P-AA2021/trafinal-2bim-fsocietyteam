from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# ejemplo de uso django-rest_framework
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from administrativo.serializers import UserSerializer, GroupSerializer, \
PersonaSerializer, BarrioSerializer, CasaSerializer, DepartamentoSerializer

# importar las clases de models.py
from administrativo.models import *

# importar los formularios de forms.py
from administrativo.forms import *

# Create your views here.
def index(request):
    """
        Listar los registros del modelo Estudiante,
        obtenidos de la base de datos.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # estudiantes
    personas = Persona.objects.all()
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'personas': personas, 'numero_personas': len(personas)}
    return render(request, 'index.html', informacion_template)
"""
CRUD PERSONA
"""
def crear_persona(request):
    """
    """
    if request.method=='POST':
        formulario = PersonaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = PersonaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearPersona.html', diccionario)

def editar_persona(request, id):
    """
    """
    persona = Persona.objects.get(pk=id)
    if request.method=='POST':
        formulario = PersonaForm(request.POST, instance=persona)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = PersonaForm(instance=persona)
    diccionario = {'formulario': formulario}

    return render(request, 'editarPersona.html', diccionario)

def eliminar_persona(request, id):
    """
    """
    persona = Persona.objects.get(pk=id)
    persona.delete()
    return redirect(index)

"""
CRUD Barrio
"""
def crear_barrio(request):
    """
    """
    if request.method=='POST':
        formulario = BarrioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = BarrioForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearBarrio.html', diccionario)

def editar_barrio(request, id):
    """
    """
    barrio = Barrio.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioForm(request.POST, instance=barrio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm(instance=barrio)
    diccionario = {'formulario': formulario}

    return render(request, 'editarBarrio.html', diccionario)

def eliminar_barrio(request, id):
    """
    """
    barrio = Barrio.objects.get(pk=id)
    barrio.delete()
    return redirect(index)
"""
CRUD CASA
"""
def crear_casa(request):
    """
    """
    if request.method=='POST':
        formulario = CasaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = CasaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearCasa.html', diccionario)

def editar_casa(request, id):
    """
    """
    casa = Casa.objects.get(pk=id)
    if request.method=='POST':
        formulario = CasaForm(request.POST, instance=casa)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = CasaForm(instance=casa)
    diccionario = {'formulario': formulario}

    return render(request, 'editarCasa.html', diccionario)

def eliminar_casa(request, id):
    """
    """
    casa = Casa.objects.get(pk=id)
    casa.delete()
    return redirect(index)
"""
CRUD DEPARTAMENTO
"""
def crear_departamento(request):
    """
    """
    if request.method=='POST':
        formulario = DepartamentoForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = DepartamentoForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearCasa.html', diccionario)

def editar_departamento(request, id):
    """
    """
    departamento = Departamento.objects.get(pk=id)
    if request.method=='POST':
        formulario = CasaForm(request.POST, instance=departamento)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = CasaForm(instance=departamento)
    diccionario = {'formulario': formulario}

    return render(request, 'editarCasa.html', diccionario)

def eliminar_departamento(request, id):
    """
    """
    departamento = Departamento.objects.get(pk=id)
    departamento.delete()
    return redirect(index)

# crear vistas a través de viewsets
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class PersonaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class BarrioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Barrio.objects.all()
    serializer_class = BarrioSerializer


class CasaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Casa.objects.all()
    serializer_class = CasaSerializer
    permission_classes = [permissions.IsAuthenticated]

class DepartamentoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    permission_classes = [permissions.IsAuthenticated]

