from django.shortcuts import render, redirect, get_object_or_404
from abrigo_animais.forms import PedidoAdocao
from abrigo_animais.forms import PedidoAdocaoForm
from animais.models import CadastroAnimal


def inicio(request):
    return render(request, "index.html")

def pagina_inicial(request):

    animais = CadastroAnimal.objects.all()

    return render(request, "pagina_inicial.html", {'animais': animais})


def card_animais(request, id):

    card = CadastroAnimal.objects.get(id = id)
    
    return render(request, "card_animais.html", {'card': card})

def pesquisar_animais(request):
  if request.method == "POST":
    pesquisa = request.POST['pesquisa']
    nome = CadastroAnimal.objects.filter(nome__contains=pesquisa)
    espécie = CadastroAnimal.objects.filter(espécie__contains=pesquisa)
    raça = CadastroAnimal.objects.filter(raça__contains=pesquisa)
    idade = CadastroAnimal.objects.filter(idade__contains=pesquisa)

    animais = nome | espécie | raça | idade
    return render(request, 'pesquisar_animais.html', {'pesquisa': pesquisa, 'animais': animais})
  else:
    return render(request,'pesquisar_animais.html')
  

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


def status(request, status_id):

    pedido = get_object_or_404(PedidoAdocao, pk=status_id)

    if request.user.is_authenticated and pedido.user == request.user:
        return render(request, 'status.html', {'pedido': pedido})
    else:
        return redirect('login')

def sobre(request):
    return render(request, "sobre.html")

def fale_conosco(request):
    return render(request, "fale_conosco.html")
