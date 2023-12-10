from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from abrigo_animais.forms import PedidoAdocaoForm, FaleConoscoForm
from animais.models import CadastroAnimal
from cadastro.models import CadastroUsuario
from abrigo_animais.models import PedidoAdocao


def inicio(request):
    return render(request, "index.html")

def pagina_inicial(request):

    animais = CadastroAnimal.objects.all()

    return render(request, "pagina_inicial.html", {'animais': animais})


def card_animais(request, id):

    card = CadastroAnimal.objects.get(id = id)
    
    return render(request, "card_animais.html", {'card': card})

def contribuinte(request):
    contribuinte = CadastroUsuario.objects.all()

    return render(request, "contribuinte.html", {'cadastro': contribuinte})

def pesquisar_animais(request):
  if request.method == "POST":
    pesquisa = request.POST['pesquisa']
    nome = CadastroAnimal.objects.filter(nome__nome__contains=pesquisa)
    espécie = CadastroAnimal.objects.filter(espécie__espécie__contains=pesquisa)
    raça = CadastroAnimal.objects.filter(raça__raça__contains=pesquisa)
    idade = CadastroAnimal.objects.filter(idade__idade__contains=pesquisa)

    animais = nome | espécie | raça | idade
    return render(request, 'pesquisar_animais.html', {'pesquisa': pesquisa, 'animais': animais})
  else:
    return render(request,'pesquisar_animais.html')
  
@login_required
def pedido_adocao(request):
        
    # Valida e salva o formulário   
    if request.method == 'POST':

            # Cria formulário
        form = PedidoAdocaoForm(request.POST)

        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('Abrigo_de_Animais')
    else:
        form = PedidoAdocaoForm()

    # Chama Template
    return render(request, 'pedido_adocao.html', {'form': form})

@login_required
def status(request, status_id):

    pedido = get_object_or_404(PedidoAdocao, pk=status_id)

    if request.user.is_authenticated and pedido.user == request.user:
        return render(request, 'status.html', {'pedido': pedido})
    else:
        return redirect('login')

def sobre(request):
    return render(request, "sobre.html")

def fale_conosco(request):
   sucesso = False   
   form = FaleConoscoForm(request.POST or None)
   if form.is_valid(): 
    sucesso = True
    form.save()
   contexto = {
      'form':form,
      'sucesso': sucesso
   }
   return render(request, "fale_conosco.html", contexto)
