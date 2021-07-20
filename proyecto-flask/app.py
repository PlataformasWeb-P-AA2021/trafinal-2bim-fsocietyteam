from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return "<p>Administración Casas y departamentos</p>"

@app.route("/laspersonas")
def las_personas():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/persona/",
            auth=('erick', '1234'))
    personas = json.loads(r.content)['results']
    numero_personas = json.loads(r.content)['count']
    return render_template("laspersonas.html", personas=personas,
    numero_personas=numero_personas)


@app.route("/losbarrios")
def los_barrios():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/barrio/",
            auth=('erick', '1234'))
    barrios = json.loads(r.content)['results']
    numero_barrios = json.loads(r.content)['count']
    return render_template("losbarrios.html", barrios=barrios,
    numero_barrios=numero_barrios)



@app.route("/lascasas")
def las_casas():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/casa/",
            auth=('erick', '1234'))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    datos2 = []
    for d in datos:
        datos2.append({'propietario':obtener_persona(d['propietario']), 'direccion':d['direccion'], 'barrio':obtener_barrio(d['barrio']), 
        'valorCasa':d['valorCasa'], 'colorCasa':d['colorCasa'], 'numCuartos':d['numCuartos'],'numPisos':d['numPisos'],
        })
    return render_template("lascasas.html", datos=datos2,
    numero=numero)




@app.route("/losdepartamentos")
def los_departamentos():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/departamento/",
            auth=('erick', '1234'))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    datos2 = []
    for d in datos:
        datos2.append({'propietario':obtener_persona(d['propietario']), 'direccion':d['direccion'], 'barrio':obtener_barrio(d['barrio']), 
        'valorDepartamento':d['valorDepartamento'], 'numCuartos':d['numCuartos'], 'valorMantenimiento':d['valorMantenimiento'],
        })
    return render_template("losdepartamentos.html", datos=datos2,
    numero=numero)

# funciones ayuda

def obtener_persona(url):
    """
    """
    r = requests.get(url, auth=('erick', '1234'))
    persona = json.loads(r.content)['nombres'] + " - " + json.loads(r.content)['apellidos'] + " - " + json.loads(r.content)['cedula'] + " - " + json.loads(r.content)['correo']
    return persona

def obtener_barrio(url):
    """
    """
    r = requests.get(url, auth=('erick', '1234'))
    barrio = json.loads(r.content)['nombreBarrio'] + " - " + json.loads(r.content)['siglas'] 
    return barrio