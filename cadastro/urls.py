from django.urls import path
from cadastro.views import cadastro_usuario

urlpatterns = [
  path('cadastro_usuario/', cadastro_usuario, name='Cadastro_Usuario')
]