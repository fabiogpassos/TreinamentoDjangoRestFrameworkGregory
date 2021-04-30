from django.contrib import admin

from .models import PontoTuristico

# Register your models here.
@admin.register(PontoTuristico)
class PontoTuristicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'aprovado')
