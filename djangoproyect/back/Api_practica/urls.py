from django.urls import path
from .views import UsuarioDbApiList, UsuarioDbApiCreate

urlpatterns = [
    path('usuarios_list/', UsuarioDbApiList.as_view(), name='usuarios_list'),
    path("usuario_create/", UsuarioDbApiCreate.as_view(), name='usuarios_create'),
]
