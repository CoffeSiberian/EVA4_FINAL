from django.db import models

# Create your models here.

class Reserva(models.Model):
    nombreResponsable = models.CharField(max_length=100, null=False)
    telefono = models.CharField(max_length=50, null=False)
    fechaReserva = models.DateField(null=False)
    horaReserva = models.DateTimeField(null=False)
    cantidadPersonas = models.IntegerField(null=False)
    estado = models.CharField(max_length=90, null=False)
    observacion = models.CharField(max_length=1000)
