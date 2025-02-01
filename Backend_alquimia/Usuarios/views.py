from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CustomUserSerializers
from .models import CustomUser
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


# Create your views here.

# vistas de ususario, 

#LOGIN
@api_view(['POST'])
def login(request):
    print(request.data)
    user = get_object_or_404(CustomUser, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"error": "invlid password"}, status=status.HTTP_400_BAD_REQUEST)
    
    token, created = Token.objects.get_or_create(user=user)
    
    serilizer = CustomUserSerializers(instance=user)

    return Response({"token": token.key, "user": serilizer.data}, status=status.HTTP_200_OK)

#Registro
@api_view(['POST'])
def register(request):
    serilizer = CustomUserSerializers(data=request.data)
    
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

#visualizar el perfil
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def perfil(request):
    print(request.user)
    serializer = CustomUserSerializers(instance=request.user)
    
    #return Response("estas logeado {}".format(request.user.username), status=status.HTTP_200_OK)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def listar_usuarios_clientes(request):
    if not request.user.is_staff:
        return Response({"error": "No tienes permisos para realizar esta acción"}, status=status.HTTP_403_FORBIDDEN)
    
    clientes = CustomUser.objects.filter(tipo_de_usuario='cliente')
    serializer = CustomUserSerializers(clientes, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)


#usar esta tambein para borar los usuarios, podes hacer que liste los usuarios con los filtros y cuando quieras borrar definitivo un usuario, mandarle la  funcion de abajo
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def filtrar_usuarios(request):
    if not request.user.is_staff:
        return Response({"error": "No tienes permisos para realizar esta acción"}, status=status.HTTP_403_FORBIDDEN)
    
    filtro = request.data.get('filtro', {})
    usuarios = CustomUser.objects.filter(**filtro)
    serializer = CustomUserSerializers(usuarios, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def eliminar_usuario(request):
    if not request.user.is_staff:
        return Response({"error": "No tienes permisos para realizar esta acción"}, status=status.HTTP_403_FORBIDDEN)
    
    filtro = request.data.get('filtro', {})
    usuario = get_object_or_404(CustomUser, **filtro)
    
    usuario.delete()
    
    return Response({"message": "Usuario eliminado correctamente"}, status=status.HTTP_200_OK)