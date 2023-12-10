from django.db import models
from django.contrib.auth.models import User
from animais.models import CadastroAnimal
from django.core.validators import MinValueValidator

class PedidoAdocao(models.Model):
    tipo_solicitação = (
        ("Aceito", "Aceito"),
        ("Recusado", "Recusado"),
        ("Em análise", "Em análise")
    )

    # Cria classe do formulario para o modelo
    #user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=120)
    email=models.EmailField()
    endereço=models.CharField(max_length=120)
    contato=models.IntegerField(validators=[MinValueValidator(0)])
    animal = models.ForeignKey(CadastroAnimal, on_delete=models.DO_NOTHING)
    solicitação=models.CharField(max_length=30, choices=tipo_solicitação)
    cuidados_com_animal=models.TextField()

    def __str__(self):
        return f"[{self.nome}] [{self.email}] [{self.endereço}] [{self.contato}] [{self.solicitação}] [{self.cuidados_com_animal}]"
    
    # Associa formulario ao modelo
    class Meta:
        verbose_name = "Formulário de Adoção de Animal"
        verbose_name_plural = "Formulários de Adoções de Animais"
        ordering = ["solicitação"]

class FaleConosco(models.Model):
  nome = models.CharField(max_length=100)
  email = models.EmailField()
  mensagem = models.TextField()

  def __str__(self) -> str:
    return f"[{self.nome}] [{self.email}] [{self.mensagem}]"
  
  class Meta: 
    verbose_name = "Formulário de contato"
    verbose_name_plural = "Formulários de contato"
    ordering = ["nome"]