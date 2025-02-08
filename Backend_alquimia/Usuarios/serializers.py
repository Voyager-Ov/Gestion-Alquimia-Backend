from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "tipo_de_usuario",
            "telefono",
            "direccion",
        ]

class PerflSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
        
       
        
       
        

