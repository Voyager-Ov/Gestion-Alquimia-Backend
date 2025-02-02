from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SuscripcionSerializers
from .models import Suscripcion
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def listar_suscripciones(request):
    if not request.user.tipo_de_usuario == 'administrador' or request.user.tipo_de_usuario == 'empleado':
        return Response({"error": "No tienes permisos para realizar esta acción"}, status=status.HTTP_403_FORBIDDEN)
    
    suscripciones = Suscripcion.objects.all()
    serializer = SuscripcionSerializers(suscripciones, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)


#usar esta tambein para borar los usuarios, podes hacer que liste los usuarios con los filtros y cuando quieras borrar definitivo un usuario, mandarle la  funcion de abajo
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def filtrar_suscripciones(request):
    if not request.user.tipo_de_usuario == 'administrador' or request.user.tipo_de_usuario == 'empleado':
        return Response({"error": "No tienes permisos para realizar esta acción"}, status=status.HTTP_403_FORBIDDEN)
    
    filtro = request.data.get('filtro', {})
    suscripciones = Suscripcion.objects.filter(**filtro)
    serializer = SuscripcionSerializers(suscripciones, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def eliminar_suscripcion(request):
    if not request.user.tipo_de_usuario == 'administrador' or request.user.tipo_de_usuario == 'empleado':
        return Response({"error": "No tienes permisos para realizar esta acción"}, status=status.HTTP_403_FORBIDDEN)
    
    filtro = request.data.get('filtro', {})
    suscripcion = get_object_or_404(Suscripcion, **filtro)
    
    suscripcion.delete()
    
    return Response({"message": "suscripcion eliminado correctamente"}, status=status.HTTP_200_OK)


@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def actualizar_suscripcion(request):
    if not request.user.tipo_de_usuario == 'administrador' or request.user.tipo_de_usuario == 'empleado':
        return Response({"error": "No tienes permisos para realizar esta acción"}, status=status.HTTP_403_FORBIDDEN)
    
    filtro = request.data.get('filtro', {})
    datos_actualizados = request.data.get('datos_actualizados', {})
    
    suscripcion = get_object_or_404(Suscripcion, **filtro)
    
    serializer = SuscripcionSerializers(suscripcion, data=datos_actualizados, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)