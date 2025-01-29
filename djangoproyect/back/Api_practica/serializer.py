from rest_framework import serializers
from pedidos.models import PedidoDb, UsuarioDb

# serializador de modelo 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioDb
        fields = "__all__"

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoDb
        fields = '__all__'
        
