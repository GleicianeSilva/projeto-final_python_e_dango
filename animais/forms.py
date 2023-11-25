from django import forms
from animais.models import CadastroAnimal

class CadastroAnimalForm(forms.ModelForm):
    class Meta:
        model = CadastroAnimal
        fields = ["nome", "espécie", "idade", "raça", "histórico_de_saúde", "foto"]
