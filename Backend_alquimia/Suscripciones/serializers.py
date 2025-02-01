from rest_framework import serializers
from .models import Suscripcion
from Usuarios.serializers import CustomUserSerializers


class SuscripcionSerializers(serializers.ModelSerializer):
    usuario = CustomUserSerializers(read_only=True)
    class Meta:
        model = Suscripcion
        fields = "__all__"