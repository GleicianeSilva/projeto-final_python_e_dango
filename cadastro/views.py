from django.shortcuts import render
from cadastro.models import CadastroUsuario
from cadastro.forms import CadastroUsuarioForm
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_admin)
def cadastro_usuario(request):
    sucesso = False
    
    # Cria formulário
    form = CadastroUsuarioForm(request.POST or None, request.FILES)
    
    # Valida e salva o formulário
    if form.is_valid():
        sucesso = True
        form.save()

    contexto = {
        "form": form,
        "sucesso": sucesso
    }
    
    # Chama Template
    return render(request, "cadastro_usuario.html", contexto)


