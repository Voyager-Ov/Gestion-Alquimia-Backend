from django.contrib import admin
from .models import PedidoDb, SubscripcionDb, UsuarioDb

# para crear un superusuario se pone en la terminal py manage.py createsuperuser

class PedidosIn(admin.TabularInline):
    model = PedidoDb
    extra = 1

# creando el registro de modelos

class PedidoAdmin(admin.ModelAdmin):
    fields = ["id", "descripcion", "fecha_recepcion", "fecha_entrega", "precio",  "estado_pedido", "estado_pago", "usuario_fk",]
    list_display = ["id", "descripcion"]
    

class SubscripcionAdmin(admin.ModelAdmin):
    fields = ["tipo", "fecha_inicio", "fecha_fin", "precio"]
    list_display = ["tipo", "precio"]
    

class UsuarioAdmin(admin.ModelAdmin):
    fields = ["id", "nombre", "apellido", "email", "telefono", "direccion", "nombre_de_usuario", "password", "tipo_de_usuario"]
    list_display = ["nombre_de_usuario", "nombre", "apellido"]
     
    
    
    
    
# se registran los modelos
admin.site.register(PedidoDb, PedidoAdmin)

admin.site.register(SubscripcionDb, SubscripcionAdmin)

admin.site.register(UsuarioDb, UsuarioAdmin)


    