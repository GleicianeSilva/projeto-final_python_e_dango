from django import forms
from .models import PedidoAdocao

class PedidoAdocaoForm(forms.ModelForm):
    class Meta:
        model = PedidoAdocao
        fields = ["nome", "email", "endereço", "contato", "solicitação", "cuidados_com_animal"]
