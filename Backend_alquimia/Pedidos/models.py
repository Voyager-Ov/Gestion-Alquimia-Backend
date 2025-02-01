from django.db import models
from Usuarios.models import CustomUser

class Pedido(models.Model):
    ESTADO_PEDIDO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
    ]
    ESTADO_PAGO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
        ('reembolsado', 'Reembolsado'),
    ]
    
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='pedidos')
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    tipo_servicio = models.TextField(max_length=1000, verbose_name="Tipo de Servicio")
    descripcion = models.TextField(max_length=1000, verbose_name="Descripción")
   
    fecha_entrega = models.DateField(verbose_name="Fecha de Entrega")
    
    estado_pedido = models.CharField(max_length=20, choices=ESTADO_PEDIDO_CHOICES, verbose_name="Estado del Pedido")
    estado_pago = models.CharField(max_length=20, choices=ESTADO_PAGO_CHOICES, verbose_name="Estado del Pago")
    
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")

    class Meta:
        db_table = "pedidos"
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
    
    def __str__(self):
        return (
            f"id: {self.id} | descripcion:  {self.descripcion} | fecha de recepcion: {self.fecha_recepcion} | precio: {self.precio} | estado de pedido: {self.estado_pedido} | estado de pago: {self.estado_pago} | usuario: {self.CustomUser_fk.username}"
        )