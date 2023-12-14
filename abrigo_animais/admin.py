from django.contrib import admin
from abrigo_animais.models import PedidoAdocao, FaleConosco

@admin.register(PedidoAdocao)
class PedidoAdocaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'solicitação')
    search_fields = ('nome', 'email')
    list_filter = ('solicitação',)

@admin.register(FaleConosco)
class FaleConoscoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'mensagem')
    search_fields = ('nome', 'email')
    list_filter = ('nome',)