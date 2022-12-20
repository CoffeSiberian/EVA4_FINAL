from django.db import models

# Create your models here.

class Reserva(models.Model):
    nombreResponsable = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50)
    fechaReserva = models.DateField()
    horaReserva = models.DateTimeField()
    cantidadPersonas = models.IntegerField()
    estado = models.CharField(max_length=90)
    observacion = models.CharField(max_length=1000)
