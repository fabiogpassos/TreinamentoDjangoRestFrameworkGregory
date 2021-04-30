from django.contrib import admin

from .models import Endereco

# Register your models here.
@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('linha1', 'cidade', 'estado', 'pais')
