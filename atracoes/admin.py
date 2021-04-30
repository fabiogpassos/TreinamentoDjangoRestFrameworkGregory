from django.contrib import admin

from .models import Atracao

# Register your models here.
@admin.register(Atracao)
class AtracaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'horario_func', 'idade_minima')
