from django.urls import path
from . import views

urlpatterns = [
    path("crear_suscripcion", views.crear_suscripcion),
    path("eliminar_suscripcion", views.eliminar_suscripcion),
    path("listar_suscripciones", views.listar_suscripciones),
    path('mis_suscripciones', views.listar_mis_suscripciones),
    path("filtrar_suscripciones", views.filtrar_suscripciones),
    path("actualizar_suscripcion", views.actualizar_suscripcion) #PUT Actualiza el Usuario, si sos admin o empleado, puedes modificar un usuario
]