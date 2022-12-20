from rest_framework import serializers
from .models import Reserva

class ReservaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'