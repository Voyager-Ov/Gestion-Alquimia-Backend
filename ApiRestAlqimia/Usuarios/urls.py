from django.urls import path
from . import views

urlpatterns = [
    # Autenticación y perfil
    path("login", views.login),  # POST: Iniciar sesión
    path("register", views.register),  # POST: Registrar un nuevo usuario
    path("perfil", views.perfil),  # POST: Obtener perfil del usuario autenticado
]