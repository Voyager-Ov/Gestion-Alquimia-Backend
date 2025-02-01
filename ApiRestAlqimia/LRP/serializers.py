from rest_framework import serializers
from .models import PedidoCliente

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoCliente
        fields = "__all__"
        
        