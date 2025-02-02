from django.urls import path
from . import views

urlpatterns = [
    # Autenticación y perfil
    path("login", views.login),  # POST: Iniciar sesión
    path("register", views.register),  # POST: Registrar un nuevo usuario
    path("perfil", views.perfil),  # POST: Obtener perfil del usuario autenticado
    path("usuarios_clientes", views.listar_usuarios_clientes),
    path("filtrar_usuarios", views.filtrar_usuarios),
    path("eliminar_usuario", views.eliminar_usuario),
    path("actualizar_usuario", views.actualizar_usuario) #PUT Actualiza el Usuario, si sos admin o empleado, puedes modificar un usuario
]