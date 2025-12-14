from django.db import models

# Create your models here.

from django.db import models

class Animal(models.Model):
    nombre = models.CharField(max_length=40)
    especie = models.CharField(max_length=40)
    edad = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=200, blank=True)

class Adoptante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    telefono = models.CharField(max_length=30, blank=True)

class Solicitud(models.Model):
    animal_nombre = models.CharField(max_length=100)
    adoptante_nombre = models.CharField(max_length=100)
    fecha_de_solicitud = models.DateField()
    estado = models.CharField(max_length=30)