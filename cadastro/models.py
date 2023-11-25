from django.db import models
from django.core.validators import MinValueValidator

class CadastroUsuario(models.Model):

    sexo_tipo = (
        ("f", "Feminino"),
        ("m", "Masculino"),
    )

    # Cria classe do formulario para o modelo
    nome_completo = models.CharField(max_length=50)
    email = models.EmailField(max_length=77)
    CPF = models.CharField(max_length=11)
    data_nascimento=models.DateField(help_text="dd/mm/aaaa")
    sexo=models.CharField(max_length=100, choices=sexo_tipo)
    contato=models.IntegerField(validators=[MinValueValidator(0)])
    cep = models.CharField(max_length=9)
    endereco = models.CharField(max_length=255)
    foto=models.ImageField(upload_to="uploads/", blank=True, null=True)

    def __str__(self):
        return f"{self.nome_completo} [{self.CPF}] [{self.data_nascimento}] [{self.sexo}] [{self.contato}] [{self.foto}]"
    
    # Associa formulario ao modelo
    class Meta:
        verbose_name = "Formulário de Cadastro de Usuário"
        verbose_name_plural = "Formulários de Cadastros de Usuários"
        ordering = ["CPF"]