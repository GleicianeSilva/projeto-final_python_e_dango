
from django.shortcuts import render
from animais.forms import CadastroAnimalForm
from animais.models import CadastroAnimal

def cadastro_animal(request):
  cadastros = CadastroAnimal.objects.all()
  sucesso = False   

   # Cria formulário
  form = CadastroAnimalForm(request.POST or None, request.FILES or None)

  # Valida e salva o formulário
  if form.is_valid(): 
      sucesso = True
      form.save()
  contexto = {
      'form':form,
      'sucesso': sucesso,
      'cadastros': cadastros
    }
  
  # Chama Template
  return render(request, 'cadastro_animal.html', contexto)
