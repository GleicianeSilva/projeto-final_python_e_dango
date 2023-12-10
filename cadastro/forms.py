from django import forms
from cadastro.models import CadastroUsuario

class CadastroUsuarioForm(forms.ModelForm):
    class Meta:
        model = CadastroUsuario
        fields = ["nome_completo", "email", "CPF", "data_nascimento", "sexo", "funcao", "contato", "cep", "endereco", "foto"]

