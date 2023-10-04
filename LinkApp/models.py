from django.db import models

STATUS = ((0, "Aguardando"), (1, "Pago"), (2, "Cancelado"), (3, "Recusado"))
DIVISAO = ((1, "1x sem juros"), (2, "2x sem juros"), (3, "3x sem juros"))
# Create your models here.


class LinkPagamento(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome")
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0, verbose_name="Status")
    url = models.URLField(max_length=200, verbose_name="Url")
    dividir = models.IntegerField(choices=DIVISAO, default=1, verbose_name="Em até")

    def __str__(self):
        return self.nome
