from django import forms
from .models import Cliente, Endereco, Entrega


class FormEndereco(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = "__all__"


class FormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"


class FormEntrega(forms.ModelForm):
    class Meta:
        model = Entrega
        fields = "__all__"
