# Generated by Django 4.2.5 on 2023-09-30 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=200, verbose_name='Rua')),
                ('cidade', models.CharField(max_length=200, verbose_name='Cidade')),
                ('bairro', models.CharField(max_length=150, verbose_name='Bairro')),
                ('numero', models.PositiveIntegerField(verbose_name='Nº')),
                ('complemento', models.CharField(blank=True, max_length=200, null=True, verbose_name='Complemento')),
                ('uf', models.CharField(max_length=2, verbose_name='UF')),
                ('cep', models.CharField(blank=True, max_length=9, null=True, verbose_name='Cep')),
            ],
        ),
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedido_numero', models.CharField(max_length=10, verbose_name='Pedido nº')),
                ('informacoes', models.TextField(max_length=300)),
                ('data_hora', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Pendente'), (1, 'Saiu para entrega'), (2, 'Entregue')], default=0, verbose_name='Status')),
                ('payment_pedido', models.IntegerField(choices=[(0, 'Pedente'), (1, 'Pago')], default=0, verbose_name='P.pago')),
                ('payment_motoboy', models.IntegerField(choices=[(0, 'Pedente'), (1, 'Pago')], default=0, verbose_name='M.pago')),
                ('valor_entrega', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FreteApp.cliente')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='endereco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FreteApp.endereco'),
        ),
    ]
