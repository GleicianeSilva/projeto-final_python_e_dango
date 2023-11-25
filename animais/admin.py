from django.contrib import admin
from animais.models import CadastroAnimal

@admin.register(CadastroAnimal)
class CadastroAnimalAdmin(admin.ModelAdmin):
  list_display = ["nome", "espécie", "idade", "raça", "foto"]
  search_fields = ["nome", "especie", "raça"]
  list_filter = ["raça"]


