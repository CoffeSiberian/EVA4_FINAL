"""EVA4_FINAL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from finalApp.views import listadoReserva, crearReserva, eliminarReserva, editarReserva, listaReservas, reserva_detalle
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('reservas/', listadoReserva, name='reservas'),
    path('crearReserva/', crearReserva, name='crearReserva'),
    path('eliminarReserva/<int:id>', eliminarReserva, name='eliminarReserva'),
    path('editarReserva/<int:id>', editarReserva, name='editarReserva'),
    path('ReservaApi/', listaReservas),
    path('ReservaApi/<int:pk>', reserva_detalle, name='detalle'),
]
