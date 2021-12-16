from django.db import models

# Create your models here.
class Evento(models.Model):
    nombre = models.CharField(max_length=45)
    ciudad = models.CharField(max_length=45)
    fecha = models.DateTimeField()
    valorEntrada = models.IntegerField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Ciudad: {self.ciudad} - Fecha: {self.fecha} - Valor Entrada: {self.valorEntrada}"
    
class Banda(models.Model):
    nombre = models.CharField(max_length=45)
    tipoMusica = models.CharField(max_length=45)
    ciudad = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    def __str__(self):
        return f"Nombre: {self.nombre} - Tipo de Música: {self.tipoMusica} - Ciudad: {self.ciudad} - Descripcion: {self.descripcion}"
class Instrumento(models.Model):
    nombre = models.CharField(max_length=45)
    tipoInstrumento = models.CharField(max_length=45)
    propietario = models.CharField(max_length=45)
    enVenta = models.BooleanField(default=False)
    def __str__(self):
        ventaString = "Si"
        if(self.enVenta == False):
            ventaString = "No"
        return f"Nombre: {self.nombre} - Tipo de Instrumento: {self.tipoInstrumento} - Propietario: {self.propietario} - En venta: {ventaString}"