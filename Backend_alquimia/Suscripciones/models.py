from django.db import models
from Usuarios.models import CustomUser


# Create your models here.
class Suscripcion(models.Model):
    TIPO_SUSCRIPCION_CHOICES = [
        ('familiar', 'Familar'),
        ('individual', 'Individual'),
        ('pareja', 'Pareja'),
        ('alquimia', 'Alquimia'),
    ]
    ESTADO_SUSCRIPCION_CHOICES = [
        ('activa', 'Activa'),
        ('desactiva', 'Desactiva'),
    ]
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='suscripcion')

    tipo_suscripcion = models.CharField(max_length=20, choices=TIPO_SUSCRIPCION_CHOICES, verbose_name="Tipo de Suscripcion")
    fecha_inicio = models.DateField(auto_now_add=True)
    fecha_fin = models.DateField(verbose_name="Fecha de Fin", null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    estado = models.CharField(max_length=20, choices=ESTADO_SUSCRIPCION_CHOICES, verbose_name="Estado")

    
    
    class Meta:
        db_table = "subscripciones"
        verbose_name = "Subscripción"
        verbose_name_plural = "Subscripciones"
    
    def __str__(self):
        return (
            f"tipo_suscripcion: {self.tipo_suscripcion} | precio: {self.precio} | fecha de inicio: {self.fecha_inicio} | fecha de fin: {self.fecha_fin} | usuario: {self.usuario} " 
        )

