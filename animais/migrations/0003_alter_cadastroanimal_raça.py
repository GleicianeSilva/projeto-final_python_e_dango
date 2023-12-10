# Generated by Django 4.2.7 on 2023-12-07 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("animais", "0002_alter_cadastroanimal_idade_alter_cadastroanimal_nome"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cadastroanimal",
            name="raça",
            field=models.CharField(
                choices=[
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
                    ("Outro", "Outro"),
                ],
                default="",
                max_length=100,
            ),
        ),
    ]
