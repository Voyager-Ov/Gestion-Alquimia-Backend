from rest_framework import serializers
from .models import Pedido
from Usuarios.serializers import CustomUserSerializers

class PedidoSerializers(serializers.ModelSerializer):
    usuario = CustomUserSerializers(read_only=True)
    class Meta:
        model = Pedido
        fields = "__all__"