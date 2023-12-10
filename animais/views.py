
from django.shortcuts import render
from animais.forms import CadastroAnimalForm
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_admin)
def cadastro_animal(request):
  sucesso = False   

   # Cria formulário
  form = CadastroAnimalForm(request.POST or None, request.FILES or None)

  # Valida e salva o formulário
  if form.is_valid(): 
      sucesso = True
      form.save()
  contexto = {
      'form':form,
      'sucesso': sucesso
    }
  
  # Chama Template
  return render(request, 'cadastro_animal.html', contexto)
