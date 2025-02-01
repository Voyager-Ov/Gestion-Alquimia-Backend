from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model



# Create your models here.
class CustomUser(AbstractUser):
    TIPO_USUARIO_CHOICES = [
        ('cliente', 'Cliente'),
        ('empleado', 'Empleado'),
        ('administrador', 'Administrador'),
    ]
    tipo_de_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES,
                                       default='cliente', verbose_name="Tipo de Usuario")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono")
    direccion = models.CharField(max_length=255, verbose_name="Dirección")
    
    def __str__(self):
        return self.username