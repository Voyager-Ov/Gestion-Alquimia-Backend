from django.contrib import admin
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    fields = ["username", "password", "first_name", "last_name", "telefono", "direccion", "tipo_de_usuario"]
    list_display = ["id", "username", "first_name", "last_name",  "tipo_de_usuario"]

admin.site.register(CustomUser, CustomUserAdmin)
