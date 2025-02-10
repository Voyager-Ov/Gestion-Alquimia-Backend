# pedidos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('crear_pedido', views.crear_pedido),
    path('listar_pedidos', views.listar_pedidos),
    path('mis_pedidos', views.listar_mis_pedidos),
    path('filtrar_pedidos', views.filtrar_pedidos),
    path('eliminar_pedido', views.eliminar_pedido),
    path('actualizar_pedido', views.actualizar_pedido),
]