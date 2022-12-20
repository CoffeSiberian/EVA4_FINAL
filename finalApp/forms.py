from django import forms

from .models import Reserva

class ReservaForm(forms.Form):

    # Definir los estados
    ESTADOS = [('reservado','RESERVADO'), ('completada','COMPLETADA'), ('anulada','ANULADA'), ('no asisten','NO ASISTEN')]

    nombreResponsable = forms.CharField(max_length=100)
    telefono = forms.CharField(max_length=50)
    fechaReserva = forms.DateField()
    horaReserva = forms.DateTimeField()
    cantidadPersonas = forms.IntegerField()
    estado = forms.CharField(widget=forms.Select(choices=ESTADOS))
    observacion = forms.CharField(max_length=1000)

    nombreResponsable.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    fechaReserva.widget.attrs['class'] = 'form-control'
    horaReserva.widget.attrs['class'] = 'form-control'
    cantidadPersonas.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-control'
    observacion.widget.attrs['class'] = 'form-control'

class ReservaForm(forms.ModelForm):

    # Definir los estados
    ESTADOS = [('reservado','RESERVADO'), ('completada','COMPLETADA'), ('anulada','ANULADA'), ('no asisten','NO ASISTEN')]
    class Meta:
        model= Reserva
        fields = '__all__'

    nombreResponsable = forms.CharField(max_length=100, required=True)
    telefono = forms.CharField(max_length=50, required=True)
    fechaReserva = forms.DateField(required=True)
    horaReserva = forms.DateTimeField(required=True)
    cantidadPersonas = forms.IntegerField(required=True, max_value=15, min_value=1)
    estado = forms.CharField(widget=forms.Select(choices=ESTADOS))
    observacion = forms.CharField(max_length=1000, required=False)

    nombreResponsable.widget.attrs['class'] = 'form-control'
    nombreResponsable.label = 'Nombre responsable'
    telefono.widget.attrs['class'] = 'form-control'
    telefono.label = 'Telefono'
    fechaReserva.widget.attrs['class'] = 'form-control'
    fechaReserva.label = 'Fecha de Reserva'
    horaReserva.widget.attrs['class'] = 'form-control'
    horaReserva.label = 'Hora de reserva'
    cantidadPersonas.widget.attrs['class'] = 'form-control'
    cantidadPersonas.label = 'Cantidad de personas'
    estado.widget.attrs['class'] = 'form-control'
    estado.label = 'Estado'
    observacion.widget.attrs['class'] = 'form-control'
    observacion.label = 'Observación'