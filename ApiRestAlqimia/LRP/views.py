from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, OrderSerializer
from .models import CustomUser, PedidoCliente
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication




@api_view(['POST'])
def login(request):
    print(request.data)
    user = get_object_or_404(CustomUser, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"error": "invlid password"}, status=status.HTTP_400_BAD_REQUEST)
    
    token, created = Token.objects.get_or_create(user=user)
    
    serilizer = UserSerializer(instance=user)

    return Response({"token": token.key, "user": serilizer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
def register(request):
    serilizer = UserSerializer(data=request.data)
    
    if serilizer.is_valid():
        serilizer.save()
        
        user = CustomUser.objects.get(username=serilizer.data['username'])
        user.first_name = request.data.get('first_name', '')
        user.last_name = request.data.get('last_name', '')
        user.telefono = request.data.get('telefono', '')
        
        user.set_password(serilizer.data['password'])
        
        user.save()
        
        token = Token.objects.create(user=user)
        
        return Response({"token": token.key, "user": serilizer.data}, status=status.HTTP_201_CREATED)
    
    return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def perfil(request):
    print(request.user)
    serializer = UserSerializer(instance=request.user)
    
    #return Response("estas logeado {}".format(request.user.username), status=status.HTTP_200_OK)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def obtener_pedidos(request):
    if not request.user.tipo_de_usuario == "administrador":
        return Response({"error": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)
    
    pedidos = PedidoCliente.objects.all()
    serializer = OrderSerializer(pedidos, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def crear_pedido(request):
    if not request.user.tipo_de_usuario == "administrador":
        return Response({"error": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)
    
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def crear_pedido_con_usuario(request):
    
    if not request.user.tipo_de_usuario == "administrador":
        return Response({"error": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)
    
    username = request.data.get('username')
    user = get_object_or_404(CustomUser, username=username)
    
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        order = serializer.save(user=user)
        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def eliminar_pedido(request):
    """
    Elimina un pedido por su ID.
    Solo los administradores pueden eliminar pedidos.
    El ID del pedido se debe enviar en el cuerpo de la solicitud.
    """
    # Verificar si el usuario es administrador
    if not request.user.tipo_de_usuario == "administrador":
        return Response(
            {"error": "No tienes permiso para realizar esta acción."},
            status=status.HTTP_403_FORBIDDEN
        )

    # Obtener el ID del pedido del cuerpo de la solicitud
    pedido_id = request.data.get('id')
    if not pedido_id:
        return Response(
            {"error": "El campo 'pedido_id' es requerido en el cuerpo de la solicitud."},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Buscar el pedido por su ID
    pedido = get_object_or_404(PedidoCliente, id=pedido_id)

    # Eliminar el pedido
    pedido.delete()

    # Devolver una respuesta exitosa
    return Response(
        {"message": f"Pedido con ID {pedido_id} eliminado correctamente."},
        status=status.HTTP_204_NO_CONTENT
    )

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def Pedidos_usuario(request):
    # Si el usuario es administrador, toma el 'username' de la URL para obtener los pedidos de ese usuario
    if request.user.tipo_de_usuario == "administrador":
        username = request.data.get('username')
        if not username:
            return Response({"error": "Username must be provided for admin users."}, status=status.HTTP_400_BAD_REQUEST)
        user = get_object_or_404(CustomUser, username=username)
        orders = PedidoCliente.objects.filter(usuario_fk=user)
    else:
        # Si el usuario es cliente, solo le devuelve sus propios pedidos
        orders = PedidoCliente.objects.filter(usuario_fk=request.user)

    # Serializa los pedidos y retorna la respuesta
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

