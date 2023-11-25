from django.contrib import admin
from abrigo_animais.models import PedidoAdocao

@admin.register(PedidoAdocao)
class PedidoAdocaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'solicitação')
    search_fields = ('nome', 'email')
    list_filter = ('solicitação',)
    