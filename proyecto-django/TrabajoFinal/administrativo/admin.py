from django.contrib import admin
from administrativo.models import Persona, Barrio, Casa, Departamento
# Register your models here.
class PersonaAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase 
    list_display = ('nombres', 'apellidos', 'cedula', 'correo')
    search_fields = ('nombre', 'cedula')

admin.site.register(Persona, PersonaAdmin)

class BarrioAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase 
    list_display = ('nombreBarrio', 'siglas')
    search_fields = ('nombreBarrio', 'siglas')

admin.site.register(Barrio, BarrioAdmin)

class CasaAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase 
    list_display = ('propietario', 'direccion','barrio','valorCasa','colorCasa','numCuartos','numPisos')
    search_fields = ('propietario', 'direccion')

admin.site.register(Casa, CasaAdmin)

class DepartamentoAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase 
    list_display = ('propietario', 'direccion','barrio','valorDepartamento','numCuartos','valorMantenimiento')
    search_fields = ('propietario', 'direccion')

admin.site.register(Departamento, DepartamentoAdmin)