from django.urls import path
from .views import UsuarioApiJson

urlpatterns = [
    path('api/usuarios_json/', UsuarioApiJson, name="usuarios_json"),
]