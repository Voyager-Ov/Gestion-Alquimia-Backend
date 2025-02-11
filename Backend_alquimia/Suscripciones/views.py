from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SuscripcionSerializers
from .models import Suscripcion
from Usuarios.models import CustomUser
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def crear_suscripcion(request):
    # Solo permiten crear suscripciones los administradores o empleados.
    if request.user.tipo_de_usuario not in ['administrador', 'empleado']:
        return Response(
            {"error": "Solo los administradores o empleados pueden crear suscripciones."},
            status=status.HTTP_403_FORBIDDEN
        )
    
    # Se espera que en el body se envíe el username del usuario al que se asignará la suscripción
    username = request.data.get('username')

    if not username:
        return Response(
            {"message": "Debe proporcionar un username para asignar la suscripción."},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    usuario_obj = get_object_or_404(CustomUser, username=username)
    
    
    # Crear la suscripción usando los datos enviados en el request.
    # Se recomienda eliminar el campo 'username' del request data antes de pasar los datos al serializer,
    # en caso de que no forme parte del modelo.
    datos = request.data.copy()
    datos.pop('username', None)  # Eliminamos el campo username si existe, ya que no es parte del modelo

    serializer = SuscripcionSerializers(data=datos)
    if serializer.is_valid():
        serializer.save(usuario=usuario_obj)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def listar_suscripciones(request):
    if not request.user.tipo_de_usuario == 'administrador' or request.user.tipo_de_usuario == 'empleado':
        return Response({"error": "No tienes permisos para realizar esta acción"}, status=status.HTTP_403_FORBIDDEN)
    
    suscripciones = Suscripcion.objects.all()
    serializer = SuscripcionSerializers(suscripciones, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def listar_mis_suscripciones(request):
    suscripciones = Suscripcion.objects.filter(usuario=request.user)
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
    
    id_suscripcion = request.data.get("id")
    if not id_suscripcion:
        return Response({"error": "Falta el ID de la suscripción"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    suscripcion = get_object_or_404(Suscripcion, id=id_suscripcion)
    suscripcion.delete()
    return Response({"message": "Suscripción eliminada correctamente"}, status=status.HTTP_200_OK)

@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def actualizar_suscripcion(request):
    print(request.data)
    if not request.user.tipo_de_usuario == 'administrador' or request.user.tipo_de_usuario == 'empleado':
        return Response({"error": "No tienes permisos para realizar esta acción"}, status=status.HTTP_403_FORBIDDEN)
    
    # Obtener el ID de la suscripción desde los datos de la solicitud
    id_suscripcion = request.data.get('id')
    if not id_suscripcion:
        return Response(
            {"error": "Debe proporcionar un ID de suscripción"},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Obtener la suscripción por su ID
    suscripcion = get_object_or_404(Suscripcion, id=id_suscripcion)

    # Actualizar la suscripción con los datos proporcionados
    serializer = SuscripcionSerializers(suscripcion, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_409_CONFLICT)