from django.shortcuts import render

from django.core.serializers import serialize
from django.http import HttpResponse

from .models import PedidoDb, SubscripcionDb, UsuarioDb

# vistas de mi api 

def CarritoApiView(request):
    return HttpResponse("hola mundo")


# vistas api django puro

def UsuarioApiJson(request):
    carro = UsuarioDb.objects.all()
    carro_serializado = serialize("json", carro)
    return HttpResponse(carro_serializado, content_type="text/json")