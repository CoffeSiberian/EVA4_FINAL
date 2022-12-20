from django.shortcuts import render, redirect
#Importar modelo empleado
from .models import Reserva
#Importar el formulario
from .forms import ReservaForm

""" Json Response"""
from django.http import JsonResponse
#Importar modelos
from finalApp.models import Reserva

""" Importar librerias para la API"""
from .serializers import ReservaSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

def Login(request):
    return render(request, 'login.html')

def listadoReserva(request):
    reservas = Reserva.objects.all()
    data = {
        'reservas' : reservas
    }
    return render(request, "reserva/reservas.html", data)

def crearReserva(request):
    form =ReservaForm()
    if (request.method == "POST"):
        form = ReservaForm(request.POST)
        if form.is_valid():
            #Rescatar los datos del formulario
            res = form.cleaned_data
            #Crear un objeto pasiente
            reserva = reserva(
                fechaReserva = res['fecha Reserva'],
                horaReserva = res['hora Reserva'],
                nombreResponsable = res['nombre Responsable'],
                telefono = res['telefono'],
                cantidadPersonas = res['cantidad Personas'],
                estado = res['estado'],
                observacion = res['observacion'],
            )
            print("Envia")
            reserva.save()
            #Limpiar el form
            form = ''
            return redirect('/reservas')
    data = {
        'form' : form,
        'titulo' : 'Crear Reserva'
    }
    return render(request, "reserva/formsReserva.html",data)

def eliminarReserva(request, id):
    reserva = Reserva.objects.get(id=id)
    reserva.delete()
    return redirect('/reservas')

def editarReserva(request, id):
    reserva = Reserva.objects.get(id=id)
    form = ReservaForm(instance=reserva)
    if (request.method == 'POST'):
        form = ReservaForm(request.POST, instance=reserva)
        if (form.is_valid()):
            form.save()
            return redirect('/reservas')
    data = {'form':form, 'titulo':'Editar reserva'}
    return render(request, "reserva/formsReserva.html", data)

# Api con datos de la base de datos y serializador
# El método GET obtiene todos los empleados
# POST a guardar un nuevo registro
@api_view(['GET', 'POST'])
def listaReservas(request):
    if (request.method == 'GET'):
        #Obtener los datos de empleados
        reservas = Reserva.objects.all()
        #Serializar los datos
        serializer = ReservaSerializers(reservas, many = True)
        #Retornar los datos serializados
        return Response(serializer.data)
    if (request.method == 'POST'):
        serializer = Reserva(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def reserva_detalle(request,pk):
    # Verificar que la reserva exista
    try:
        reserva = Reserva.objects.get(pk=pk)
    except reserva.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    # GET = Obtener los datos de las reservas X
    if (request.method == 'GET'):
        serializer = ReservaSerializers(reserva)
        return Response(serializer.data)

    #PUT = Actualizar un registro
    if (request.method == 'PUT'):
        serializer = ReservaSerializers(reserva, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    #Delete = Eliminar un registro
    if (request.method == 'DELETE'):
        reserva.delete()
    return Response(status=status.HTTP_400_BAD_REQUEST)