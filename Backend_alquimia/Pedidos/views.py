# pedidos/views.py
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .serializers import PedidoSerializers
from .models import Pedido
from Usuarios.models import CustomUser

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def crear_pedido(request):
    # Solo administradores o empleados pueden crear pedidos
    if request.user.tipo_de_usuario not in ['administrador', 'empleado']:
        return Response(
            {"error": "Solo personal autorizado puede crear pedidos"},
            status=status.HTTP_403_FORBIDDEN
        )
    
    # Obtener username del cliente asociado al pedido
    username = request.data.get('username')
    if not username:
        return Response(
            {"error": "Debe proporcionar un username de cliente"},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    cliente = get_object_or_404(CustomUser, username=username)
    
    # Crear pedido asociado al cliente
    serializer = PedidoSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save(usuario=cliente)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def listar_pedidos(request):
    # Solo administradores/empleados ven todos los pedidos
    if request.user.tipo_de_usuario not in ['administrador', 'empleado']:
        return Response(
            {"error": "No tienes permisos para ver todos los pedidos"},
            status=status.HTTP_403_FORBIDDEN
        )
    
    pedidos = Pedido.objects.all()
    serializer = PedidoSerializers(pedidos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def listar_mis_pedidos(request):
    # Usuarios normales ven solo sus pedidos
    pedidos = Pedido.objects.filter(usuario=request.user)
    serializer = PedidoSerializers(pedidos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def filtrar_pedidos(request):
    if request.user.tipo_de_usuario not in ['administrador', 'empleado']:
        return Response(
            {"error": "No tienes permisos para filtrar pedidos"},
            status=status.HTTP_403_FORBIDDEN
        )
    
    filtro = request.data.get('filtro', {})
    pedidos = Pedido.objects.filter(**filtro)
    serializer = PedidoSerializers(pedidos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def eliminar_pedido(request):
    if request.user.tipo_de_usuario not in ['administrador', 'empleado']:
        return Response(
            {"error": "No tienes permisos para eliminar pedidos"},
            status=status.HTTP_403_FORBIDDEN
        )
    
    filtro = request.data.get('filtro', {})
    pedido = get_object_or_404(Pedido, **filtro)
    pedido.delete()
    return Response({"message": "Pedido eliminado correctamente"}, status=status.HTTP_200_OK)

@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def actualizar_pedido(request):
    if request.user.tipo_de_usuario not in ['administrador', 'empleado']:
        return Response(
            {"error": "No tienes permisos para actualizar pedidos"},
            status=status.HTTP_403_FORBIDDEN
        )
    
    filtro = request.data.get('filtro', {})
    datos_actualizados = request.data.get('datos_actualizados', {})
    
    pedido = get_object_or_404(Pedido, **filtro)
    serializer = PedidoSerializers(pedido, data=datos_actualizados, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)