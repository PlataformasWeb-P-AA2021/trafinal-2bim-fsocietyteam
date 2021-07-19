from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('ver/casas',views.ver_casas,
            name='ver_casas'),
        path('ver/departamentos',views.ver_departamentos,
            name='ver_departamentos'),
        # Rutas crear
        path('crear/persona', views.crear_persona,
            name='crear_persona'),
        path('crear/barrio', views.crear_barrio,
            name='crear_barrio'),
        path('crear/casa', views.crear_casa,
            name='crear_casa'),
        path('crear/departamento', views.crear_departamento,
            name='crear_departamento'),
        # Rutas editar
        path('editar_casa/<int:id>', views.editar_casa,
            name='editar_casa'),
        path('editar_departamento/<int:id>', views.editar_departamento,
            name='editar_departamento'),
        # Rutas eliminar
        path('eliminar/casa/<int:id>', views.eliminar_casa,
            name='eliminar_casa'),
        path('eliminar/departamento/<int:id>', views.eliminar_departamento,
            name='eliminar_departamento'),
        # numeros telefonicos
        path('saliendo/logout/', views.logout_view, name="logout_view"),
        path('entrando/login/', views.ingreso, name="login"),
        
 ]