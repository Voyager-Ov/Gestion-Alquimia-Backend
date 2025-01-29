from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response



# Create your views here.

@api_view(['post'])
def login(request):
    return Response({})

@api_view(['post'])
def register(request):
    return Response({})

@api_view(['post'])
def perfil(request):
    return Response({})