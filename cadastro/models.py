from django.db import models
from django.forms import CharField
from django.core.validators import MinValueValidator

class CadastroUsuario(models.Model):

    sexo_tipo = (
        ("f", "Feminino"),
        ("m", "Masculino"),
    )
    
    tipo_funcao = (
        ("c", "Cuidador"),
        ("v", "Voluntário"),
    )

    # Cria classe do formulario para o modelo
    nome_completo = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=77)
    CPF = models.CharField(max_length=11)
    data_nascimento = models.DateField(help_text="dd/mm/aaaa")
    sexo = models.CharField(max_length=10, choices=sexo_tipo)
    funcao = models.CharField(max_length=10, choices=tipo_funcao)
    contato = models.IntegerField(validators=[MinValueValidator(0)])
    cep = models.CharField(max_length=9)
    endereco = models.CharField(max_length=255)
    foto = models.ImageField(upload_to="uploads/", blank=True, null=True)

    def __str__(self):
        return f"{self.nome_completo} [{self.CPF}] [{self.data_nascimento}] [{self.sexo}] [{self.funcao}] [{self.contato}] [{self.foto}]"
    
    # Associa formulario ao modelo
    class Meta:
        verbose_name = "Formulário de Cadastro do Contribuinte"
        verbose_name_plural = "Formulários de Cadastros dos Contribuintes"
        ordering = ["CPF"]