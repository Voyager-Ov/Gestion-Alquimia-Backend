from django.urls import path, re_path
from . import views

urlpatterns = [
    

    # Pedidos
    re_path("pedidos", views.obtener_pedidos),  # GET: Obtener todos los pedidos (solo administrador)
    re_path("crear-pedido", views.crear_pedido),  # POST: Crear un pedido (solo administrador)
    re_path("crear-pedido-usuario", views.crear_pedido_con_usuario),  # POST: Crear un pedido para un usuario específico (solo administrador)
    re_path("eliminar-pedido", views.eliminar_pedido),  # DELETE: Eliminar un pedido por ID (solo administrador)
    re_path("Pedidosusuario", views.Pedidos_usuario),  # GET: Obtener pedidos de un usuario (propios o de otro usuario si es administrador)
]