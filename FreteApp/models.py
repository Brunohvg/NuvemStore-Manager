from django.db import models
from django.contrib.auth.models import User
from secrets import token_urlsafe

# Create your models here.
STATUS = ((0, "Pendente"), (1, "Saiu para entrega"), (2, "Entregue"), (3, "Cancelada"))

STATUS_PAYMENT = ((0, "Pedente"), (1, "Pago"), (2, "Estorno"))


class Endereco(models.Model):
    logradouro = models.CharField(max_length=200, verbose_name="Rua")
    cidade = models.CharField(max_length=200, verbose_name="Cidade")
    bairro = models.CharField(max_length=150, verbose_name="Bairro")
    numero = models.PositiveIntegerField(verbose_name="Nº")
    complemento = models.CharField(
        max_length=200, verbose_name="Complemento", blank=True, null=True
    )
    uf = models.CharField(max_length=2, verbose_name="UF")
    cep = models.CharField(max_length=9, verbose_name="Cep", blank=True, null=True)

    def __str__(self):
        return f"{self.logradouro}, {self.numero}, {self.cidade}, {self.uf}, {self.complemento}"


class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Entrega(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pedido_numero = models.CharField(max_length=10, verbose_name="Pedido nº")
    informacoes = models.TextField(max_length=300, blank=True, null=True)
    data_hora = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0, verbose_name="Status")
    payment_pedido = models.IntegerField(
        choices=STATUS_PAYMENT, default=0, verbose_name="P.pago"
    )
    payment_motoboy = models.IntegerField(
        choices=STATUS_PAYMENT, default=0, verbose_name="M.pago"
    )
    valor_entrega = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    identificador = models.CharField(max_length=24, null=True, blank=True)

    def endereco_entrega(self):
        return self.cliente.endereco

    def save(self, *args, **kwargs):
        if not self.identificador:
            self.identificador = token_urlsafe(16)

        super(Entrega, self).save(*args, **kwargs)

    def __str__(self):
        return f"Entrega para {self.cliente.nome} em {self.endereco_entrega()}"
