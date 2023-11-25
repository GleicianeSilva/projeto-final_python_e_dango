# Generated by Django 4.2.7 on 2023-11-22 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CadastroUsuario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome_completo", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=77)),
                ("CPF", models.IntegerField(max_length=11)),
                ("data_nascimento", models.DateField(help_text="dd/mm/aaaa")),
                (
                    "sexo",
                    models.CharField(
                        choices=[("f", "Feminino"), ("m", "Masculino")], max_length=100
                    ),
                ),
                ("contato", models.CharField(max_length=16)),
                ("cep", models.CharField(max_length=9)),
                ("endereco", models.CharField(max_length=255)),
                ("numero", models.IntegerField()),
                ("cidade", models.CharField(max_length=102)),
                ("estado", models.CharField(max_length=2)),
                (
                    "imagens",
                    models.ImageField(blank=True, null=True, upload_to="uploads/"),
                ),
            ],
            options={
                "verbose_name": "Formulário de Cadastro de Usuário",
                "verbose_name_plural": "Formulários de Cadastros de Usuários",
                "ordering": ["CPF"],
            },
        ),
    ]