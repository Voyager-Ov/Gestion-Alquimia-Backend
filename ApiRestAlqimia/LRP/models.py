from django.db import models


# Create your models here.

class PedidoCliente(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id")
    descripcion = models.CharField(max_length=1000, verbose_name="Descripción")
    fecha_recepcion = models.DateField(verbose_name="Fecha de Recepción")
    fecha_entrega = models.DateField(verbose_name="Fecha de Entrega")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
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
    estado_pedido = models.CharField(max_length=20, choices=ESTADO_PEDIDO_CHOICES, verbose_name="Estado del Pedido")
    estado_pago = models.CharField(max_length=20, choices=ESTADO_PAGO_CHOICES, verbose_name="Estado del Pago")

    # relaciones, no se permite que se elimine un usuario si tiene pedidos asociados
    # hay que cambiarlo para que no se pueda eliminar un usuario si tiene pedidos activos
    
  
    
    class Meta:
        db_table = "pedidos"
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
    
    def __str__(self):
        return (
            f"id: {self.id} | descripcion:  {self.descripcion} | fecha de recepcion: {self.fecha_recepcion} | precio: {self.precio} | estado de pedido: {self.estado_pedido} | estado de pago: {self.estado_pago} | usuario: {self.CustomUser_fk.username}"
        )

class SubscripcionCliente(models.Model):
    tipo = models.CharField(max_length=20, verbose_name="Tipo de Plan")
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio")
    fecha_fin = models.DateField(verbose_name="Fecha de Fin")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")

    
    
    class Meta:
        db_table = "subscripciones"
        verbose_name = "Subscripción"
        verbose_name_plural = "Subscripciones"
    
    def __str__(self):
        return (
            f"tipo: {self.tipo} | precio: {self.precio} | fecha de inicio: {self.fecha_inicio} | fecha de fin: {self.fecha_fin} | usuario: {self.get_username()} " 
        )

