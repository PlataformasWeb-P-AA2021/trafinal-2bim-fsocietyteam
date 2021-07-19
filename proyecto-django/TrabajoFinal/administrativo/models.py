from django.db import models
from django.db.models.base import Model

# Create your models here.


class Persona(models.Model):
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)
    correo = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.nombres,
                                self.apellidos)


class Barrio(models.Model):
    nombreBarrio = models.CharField(max_length=30)
    siglas = models.CharField(max_length=7)

    def __str__(self):
        return "%s %s" % (self.nombreBarrio,
                          self.siglas)


class Casa(models.Model):
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE,
                                    related_name="casas")
    direccion = models.CharField(max_length=50)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE,
                               related_name="casas")
    valorCasa = models.FloatField()
    colorCasa = models.CharField(max_length=20)
    numCuartos = models.IntegerField()
    numPisos = models.IntegerField()

    def __str__(self):
        return "%s - %s -%s - %.2f - %s - %d - %d -" % (self.propietario,
                                                        self.direccion, self.barrio, self.valorCasa,
                                                        self.colorCasa, self.numCuartos, self.numPisos)


class Departamento(models.Model):
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE,
                                    related_name="departamentos")
    direccion = models.CharField(max_length=50)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE,
                               related_name="departamentos")
    valorDepartamento = models.FloatField()
    numCuartos = models.IntegerField()
    valorMantenimiento = models.FloatField()

    def __str__(self):
        return "%s - %s - %s - %.2f - %d - %.2f " % (self.nombreBarrio,
                                                     self.direccion, self.barrio, self.valorDepartamento,
                                                     self.numCuartos, self.valorMantenimiento)
