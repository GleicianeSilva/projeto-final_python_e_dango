from django.shortcuts import render
from cadastro.forms import CadastroUsuarioForm

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


