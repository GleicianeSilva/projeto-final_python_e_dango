
from django.shortcuts import render
from animais.forms import CadastroAnimalForm

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
