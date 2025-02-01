from django.contrib import admin
from .models import Pedido

# Register your models here.
class PedidoAdmin(admin.ModelAdmin): 
    fields = ["usuario", "descripcion", "tipo_servicio",
              "fecha_entrega", "precio", "estado_pedido", "estado_pago"]
    list_display = [ "descripcion", "tipo_servicio", "fecha_pedido", "precio"]

admin.site.register(Pedido, PedidoAdmin)