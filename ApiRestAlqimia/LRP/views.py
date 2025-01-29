from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import CustomUser
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



