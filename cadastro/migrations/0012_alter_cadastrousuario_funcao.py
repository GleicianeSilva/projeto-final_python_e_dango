# Generated by Django 4.2.7 on 2023-12-10 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cadastro", "0011_alter_cadastrousuario_funcao"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cadastrousuario",
            name="funcao",
            field=models.CharField(
                choices=[("", "Cuidador"), ("", "Voluntário")], max_length=10
            ),
        ),
    ]