from django.shortcuts import render

# api
from rest_framework import generics, viewsets

#modelos
from pedidos.models import PedidoDb, UsuarioDb

#serializador
from .serializer import PedidoSerializer, UserSerializer

# Create your views here.

class UsuarioDbApiList(generics.ListAPIView):
    queryset = UsuarioDb.objects.all()
    serializer_class = UserSerializer


class UsuarioDbApiCreate(generics.CreateAPIView):
    queryset = UsuarioDb.objects.all()
    serializer_class = UserSerializer
    
class UsuarioDbApiRetrive(generics.RetrieveAPIView):
    queryset = UsuarioDb.objects.all()
    serializer_class = UserSerializer
    
class UsuarioDbApiDelete(generics.DestroyAPIView):
    queryset = UsuarioDb.objects.all()
    serializer_class = UserSerializer
    
    
# view sets

class PedidoDbApiViewSet(viewsets.ModelViewSet):
    queryset = PedidoDb.objects.all()
    serializer_class = PedidoSerializer