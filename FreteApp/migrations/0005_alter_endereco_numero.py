# Generated by Django 4.2.5 on 2023-09-28 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FreteApp', '0004_endereco_cep_alter_endereco_bairro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='numero',
            field=models.PositiveIntegerField(verbose_name='Nº'),
        ),
    ]
