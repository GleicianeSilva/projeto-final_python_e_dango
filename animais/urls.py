from django.urls import path
from animais.views import cadastro_animal

app_name = 'animais'

urlpatterns = [
  path('cadastro_animal/', cadastro_animal, name='Cadastro_Animal'),
]
