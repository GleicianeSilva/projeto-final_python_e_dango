from django.views.generic.edit import CreateView
from login.forms import CredencialUsuarioForm
from django.urls import reverse_lazy


class Credencial(CreateView):
  template_name = 'cadastro_usuario.html'
  form_class = CredencialUsuarioForm
  success_url = reverse_lazy('Login')