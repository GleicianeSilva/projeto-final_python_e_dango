from django.contrib import admin

from cadastro.models import CadastroUsuario

@admin.register(CadastroUsuario)

class CadastroUsuarioAdmin(admin.ModelAdmin):
    list_display = ["nome_completo", "email", "CPF", "data_nascimento", "sexo", "contato", "foto"]
    search_fields = ["nome", "CPF"]
    list_filter = ["CPF"]
