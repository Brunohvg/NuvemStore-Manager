# Generated by Django 4.2.5 on 2023-10-05 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FreteApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrega',
            name='informacoes',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
