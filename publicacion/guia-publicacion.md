# Guía de Levantamiento de proyecto Django en Nginx
## Requisitos previos

* Trabajar en un ambiente Linux
* Tener instalado python
* Django 
* Nginx
* Gunicorn
* Mysql
* Editor de textos
* Xampp
* Navegador web

## Versionamiento
En cuanto software y tecnologías empleadas para el desarrollo se necesitó un computador con sistema operativo GNU/Linux Ubuntu en su versión 20.04,
el lenguaje de programación fue Python en su versión 3.8. Las librerías que se emplearon fueron las siguientes:
* Django
* Corsheaders
* Rest_Framework
* Gunicorn
Finalmente como sevidor web Nginx versión 1.18.0

## Proceso
### Paso 1: Configuración proyecto Django
Una vez que hemos culminado nuestro proyecto Django se realizo las siguiente configuración:
1. Instalar la librería gunicorn con el comando `pip install gunicorn`
2. En nuestro archivo _settings.py_ se agregó en la variable `ALLOWED_HOSTS = ["0.0.0.0", "127.0.0.1"]`. Agregamos también la variable `STATIC_ROOT = os.path.join(BASE_DIR,'static/')`
1. En el archivo _urls.py_ del proyecto se agrega lo siguiente: `from django.contrib.staticfiles.urls import staticfiles_urlpatterns` en las importaciones y `urlpatterns += staticfiles_urlpatterns()` se concatena urslpatterns ya creado.
1. Seguidamente se recopila el contenido estático en la carpeta _static_ con el siguiente comando: `python3 manage.py collectstatic`

### Paso 2: Levantamiento del proyecto con Gunicorn
1. Para el levantamiento del proyecto se lo realiza con el siguiente comando: `gunicorn --bind 0.0.0.0:8000 proyecto1.wsgi`, en donde _proyecto1_ es el nombre de nuestro proyecto. Cabe recalcar que con este paso nuestro proyecto debe estar funcionando en nuestro navegador web.
1. Seguidamente para iniciar el proceso de enlazar el servidor nginx mediante gunicorn con el proyecto Django. Se crea un archivo con la extensión **.service**, para crear el archivo se debe usar el siguiente comando:  `sudo touch /etc/systemd/system/proyecto1.service`.
1. Editamos el archivo creado con el siguiente comando: `sudo nano /etc/systemd/system/proyecto1.service`. En el archivo se debe agregar la siguiente información:
> 
``` 
[Unit]
# metadatos necesarios
Description=gunicorn daemon
After=network.target

[Service]
# usuario del sistema operativo que ejecutará el proceso
User=usuario-sistema-operativo
# el grupo del sistema operativo que permite la comunicación a desde el servidor web-nginx con gunicorn. No se debe cambiar el valor
Group=www-data

# a través de la variable WorkingDirectory se indica la dirección absoluta del proyecto de Django
WorkingDirectory=/home/usuario-sistema/carpeta/proyectos/nombre-proyecto

# En Environment se indica el path de python
# Ejemplo 1: /usr/bin/python3.9
# Ejemplo 2: (Opcional, con el uso de entornos virtuales) /home/usuario/entornos/entorno01/bin
Environment="PATH=agregar-path-python"

# Detallar el comando para iniciar el servicio
ExecStart=path-python/bin/gunicorn --workers 3 --bind unix:application.sock -m 007 proyectoDjango.wsgi:application

# Donde: aplicacion.sock es el nombre del archivo que se debe crear en el directorio del proyecto; proyectoDjango el nombre del proyecto que se intenta vincular con nginx.
# La expresión /bin/gunicorn no se debe modificar.

[Install]
# esta sección será usada para indicar que el servicio puede empezar cuando se inicie el sistema operativo. Se sugiere no cambiar el valor dado.
WantedBy=multi-user.target
```

4. Para iniciar y habilitar el proceso se realiza con los siguientes comandos: 

```
sudo systemctl start proyecto1
sudo systemctl enable proyecto1
```
Es importante mencionar que **proyecto1** es el nombre del archivo que se creo con la extensión _.sevice_

5. Para verificar que este en funcionamiento usar el siguiente comando:

`sudo systemctl status proyecto1`

6. Verificar en nuestra carpeta Django que se cree el archivo _application.sock_

### Parte 3: Configuración del servidor web Nginx
1. Se crea un archivo llamado **_sites-available_** de nginx, la ruta para acceder a este es la siguiente:

`/etc/nginx/sites-available/` 

esta se debe acceder con permisos de administrador (sudo).

2. El comando para crear este archivo desde la terminal es:

`sudo touch /etc/nginx/sites-available/proyecto1`

en donde se debe añadir con el comando:

`sudo nano/etc/nginx/sites-available/proyecto1`

la siguiente estructura:

```
server {
    listen 81;
    server_name localhost;
    
    location / {
        include proxy_params;
        proxy_pass http://unix:/ruta/al/archivo/sock/application.sock;
    }

    
    location /static/ {
        root /ruta/a/la/carpeta/staticos/del/proyecto-django/static/;
    }

}

```

3. Se debe iniciar un enlace simbólico del archivo creado en el directorio **_sites-available_**, con el comando:

`sudo ln -s /etc/nginx/sites-available/proyecto01 /etc/nginx/sites-enabled`

4. Ejecutar el servicio de nginx con el comando:

`sudo service nginx start`

5. Finalmente en un navegador web se debe acceder con la siguientes direcciones:
* http://localhost:81
* http://0.0.0.0:81
* http://127.0.0.0:81

Con estas direcciones debemos observar nuestro proyecto correctamente en ejecución. 