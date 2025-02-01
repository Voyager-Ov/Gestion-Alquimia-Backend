from django.contrib import admin
from .models import Suscripcion

# Register your models here.
class SuscripcionAdmin(admin.ModelAdmin):
    fields = ["usuario", "tipo_suscripcion", "fecha_fin", "precio"]
    list_display = ["id", "tipo_suscripcion", "fecha_inicio", "fecha_fin", "precio"]

admin.site.register(Suscripcion, SuscripcionAdmin)