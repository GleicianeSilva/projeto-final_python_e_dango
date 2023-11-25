# Generated by Django 4.2.7 on 2023-11-25 02:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("animais", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cadastroanimal",
            name="idade",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
        migrations.AlterField(
            model_name="cadastroanimal",
            name="nome",
            field=models.CharField(max_length=150),
        ),
    ]
