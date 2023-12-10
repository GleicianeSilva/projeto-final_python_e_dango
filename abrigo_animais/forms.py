from dataclasses import fields
from django import forms
from .models import PedidoAdocao, FaleConosco

class PedidoAdocaoForm(forms.ModelForm):
    class Meta:
        model = PedidoAdocao
        fields = ["nome", "email", "endereço", "contato", "animal", "solicitação", "cuidados_com_animal"]
class FaleConoscoForm(forms.ModelForm):
    class Meta:
        model = FaleConosco
        fields = ["nome", "email", "mensagem"]