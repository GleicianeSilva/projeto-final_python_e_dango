from django.db import models
from django.core.validators import MinValueValidator

class CadastroAnimal(models.Model):
    tipo_espécie = (
        ("Cachorro", "Cachorro"),
        ("Gato", "Gato"),
        ("Outro", "Outro")
    )
    tipo_raça = (
        ("Akita", "Akita"),
        ("Angorá Turco", "Angorá Turco"),
        ("Bobtail Americano", "Bobtail Americano"),
        ("Chihuahua", "Chihuahua"),
        ("Gato Europeu", "Gato Europeu"),
        ("Maltês", "Maltês"),
        ("Mau Egipcioa", "Mau Egipcio"),
        ("Poodle", "Poodle"),
        ("Siamês", "Siamês"),
        ("Siberiano", "Siberiano"),
        ("Shih Tzu", "Shih Tzu"),
        ("Yorkshire Terrie", "Yorkshire Terrie"),
        ("Outro", "Outro")
    )

    # Cria classe do formulario para o modelo
    nome = models.CharField(max_length=150)
    espécie=models.CharField(max_length=50, choices=tipo_espécie)
    idade=models.IntegerField(validators=[MinValueValidator(0)])
    raça=models.CharField(max_length=100, choices=tipo_raça)
    histórico_de_saúde=models.TextField()
    foto=models.ImageField(upload_to="uploads/", blank=True, null=True)

    def __str__(self):
        return f"[{self.nome}] [{self.espécie}] [{self.idade}] [{self.raça}] [{self.histórico_de_saúde}] [{self.foto}]"
    
    # Associa formulario ao modelo
    class Meta:
        verbose_name = "Formulário de Cadastro de Animal"
        verbose_name_plural = "Formulários de Cadastros de Animais"
        ordering = ["idade"]