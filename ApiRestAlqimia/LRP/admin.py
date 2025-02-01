from django.contrib import admin
from .models import PedidoCliente, SubscripcionCliente

# Register your models here.


class PedidoAdmin(admin.ModelAdmin):
    fields = ["id", "descripcion", "fecha_recepcion", "fecha_entrega", "precio",  "estado_pedido", "estado_pago", "usuario_fk",]
    list_display = ["id", "descripcion"]
    

class SubscripcionAdmin(admin.ModelAdmin):
    fields = ["tipo", "fecha_inicio", "fecha_fin", "precio", "usuario_fk"]
    list_display = ["tipo", "precio"]
    

# se registran los modelos
admin.site.register(PedidoCliente, PedidoAdmin)

admin.site.register(SubscripcionCliente, SubscripcionAdmin)



    