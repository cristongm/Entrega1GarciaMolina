from django.db import models

# Create your models here.
class Evento(models.Model):
    ciudad = models.CharField(max_length=45)
    fecha = models.DateTimeField()
    valorEntrada = models.IntegerField()
    
class Banda(models.Model):
    nombre = models.CharField(max_length=45)
    tipoMusica = models.CharField(max_length=45)
    ciudad = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)

class Instrumento(models.Model):
    nombre = models.CharField(max_length=45)
    tipoInstrumento = models.CharField(max_length=45)
    propietario = models.CharField(max_length=45)
    enVenta = models.BooleanField()
    