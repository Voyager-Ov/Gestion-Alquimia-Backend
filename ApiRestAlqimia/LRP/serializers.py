from rest_framework import serializers
from .models import CustomUser, PedidoCliente

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "email", "password", "tipo_de_usuario"]
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoCliente
        fields = ["id", "descripcion", "fecha_recepcion", "fecha_entrega", "precio", "estado_pedido", "estado_pago"]
