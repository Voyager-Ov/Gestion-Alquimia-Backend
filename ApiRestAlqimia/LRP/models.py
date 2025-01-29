from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    TIPO_USUARIO_CHOICES = [
        ('cliente', 'Cliente'),
        ('administrador', 'Administrador'),
    ]
    tipo_de_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES,
                                       default='cliente', verbose_name="Tipo de Usuario")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono")
    direccion = models.CharField(max_length=255, verbose_name="Dirección")

    
# Create your models here.

class PedidoCliente(models.Model):
    id = models.CharField(max_length=1000, primary_key=True, unique=True, verbose_name="ID")
    descripcion = models.CharField(max_length=1000, verbose_name="Descripción")
    fecha_recepcion = models.DateField(verbose_name="Fecha de Recepción")
    fecha_entrega = models.DateField(verbose_name="Fecha de Entrega")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    estado_pedido = models.CharField(max_length=20, verbose_name="Estado del Pedido")
    estado_pago = models.CharField(max_length=20, verbose_name="Estado del Pago")
    
    # relaciones, no se permite que se elimine un usuario si tiene pedidos asociados
    # hay que cambiarlo para que no se pueda eliminar un usuario si tiene pedidos activos
    usuario_fk = models.ForeignKey("CustomUser", on_delete=models.CASCADE, verbose_name="Usuario")
    
    class Meta:
        db_table = "pedidos"
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
    
    def __str__(self):
        return (
            f"id: {self.id} | "
            f"fecha de recepcion: {self.fecha_recepcion} | "
            f"descripcion: {self.descripcion}"
        )

class SubscripcionCliente(models.Model):
    tipo = models.CharField(max_length=20, verbose_name="Tipo de Plan")
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio")
    fecha_fin = models.DateField(verbose_name="Fecha de Fin")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    
    usuario_fk = models.ForeignKey("CustomUser", on_delete=models.CASCADE, verbose_name="Usuario")

    
    class Meta:
        db_table = "subscripciones"
        verbose_name = "Subscripción"
        verbose_name_plural = "Subscripciones"
    
    def __str__(self):
        return (
            f"tipo: {self.tipo} | precio: {self.precio} | fecha de inicio: {self.fecha_inicio} | fecha de fin: {self.fecha_fin}"
        )

