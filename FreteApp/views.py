from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .Apis.calculador_frete import CalculadoraFrete
from django.contrib import messages
from .forms import FormEndereco, FormCliente, FormEntrega
from .models import Entrega, Endereco, Cliente
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError

# Configurações
CEP_PADRAO = "30170130"  # Valor do CEP padrão


def converter_valor(valor):
    valor = valor.replace(",", ".")
    valor = round(float(valor), 2)  # Arredonda o valor para duas casas decimais
    return valor


@login_required
def dashboard(request):
    return render(request, "FreteApp/dashboard.html")


@login_required
def calculadora(request):
    if request.method == "POST":
        return handle_post(request)
    else:
        return render(request, "FreteApp/cotacoes.html")


@login_required
def handle_post(request):
    data = {
        "cep": request.POST.get("cep"),
        "comprimento": request.POST.get("comprimento"),
        "largura": request.POST.get("largura"),
        "altura": request.POST.get("altura"),
        "peso": request.POST.get("peso"),
    }
    if data["cep"]:
        return handle_end(request, data)
    else:
        return render(request, "FreteApp/cotacoes.html")


@login_required
def handle_end(request, data):
    calculadora = CalculadoraFrete(CEP_PADRAO)
    cep = data["cep"]
    if cep:
        endereco = calculadora.consultar_endereco(cep)
        if not endereco:
            messages.error(request, f"Atenção: o CEP {cep} é inválido.")
        else:
            end_data = {
                "rua": endereco["street"],
                "bairro": endereco["district"],
                "cidade": endereco["city"],
                "uf": endereco["stateShortname"],
                "cep": endereco["zipcode"],
                "complemento": endereco["complement"],
            }
            return handle_valor_correio(request, data, end_data)
    return render(request, "FreteApp/cotacoes.html")


@login_required
def handle_valor_correio(request, data, end_data):
    calculadora = CalculadoraFrete(CEP_PADRAO)
    cep = data["cep"]
    peso = data["peso"]
    comprimento = data["comprimento"]
    largura = data["largura"]
    altura = data["altura"]

    dimensoes_max = 200
    soma = float(comprimento) + float(largura) + float(altura)

    try:
        if soma > dimensoes_max:
            raise ValueError("As dimensões excedem o limite máximo permitido.")

        data_correio = calculadora.consultar_valor_correio(
            cep, peso, comprimento, largura, altura
        )

        dados_sedex = data_correio[0]
        dados_pac = data_correio[1]

        valor_sedex = converter_valor(dados_sedex["Valor"])
        valor_pac = converter_valor(dados_pac["Valor"])

        correio_data = {
            "valor_sedex": valor_sedex,
            "prazo_sedex": dados_sedex["PrazoEntrega"],
            "valor_pac": valor_pac,
            "prazo_pac": dados_pac["PrazoEntrega"],
        }

        return handle_valor_motoboy(request, data, end_data, correio_data)

    except ValueError as e:
        error_message = str(e)
        messages.error(
            request,
            f"Erro: {error_message} => Soma das dimensões não pode ultrapassar 200 cm.",
        )
        return render(request, "FreteApp/cotacoes.html")


@login_required
def handle_valor_motoboy(request, data, end_data, correio_data):
    calculador = CalculadoraFrete(CEP_PADRAO)
    cep = data["cep"]
    if cep:
        valor_motoboy = calculador.consultar_valor_motoboy(cep)
        motoboy_data = {"valor_motoboy": valor_motoboy}
        form_endereco = FormEndereco()
        form_cliente = FormCliente()
        form_entrega = FormEntrega()
        context = {
            **correio_data,
            **end_data,
            **motoboy_data,
            "form_endereco": form_endereco,
            "form_cliente": form_cliente,
            "form_entrega": form_entrega,
        }
        return render(request, "FreteApp/cotacoes.html", context)
    return render(request, "FreteApp/cotacoes.html")


def listar_entregas(request):
    todas_entregas = Entrega.objects.all()
    t_entregas = {
        "todas_entregas": todas_entregas,
    }

    if request.method == "POST":
        try:
            create_endereco(request)
        except ValidationError as e:
            messages.error(request, f"Atenção: o CEP {e} é inválido.")
            return HttpResponseServerError(f"Erro ao criar endereço: {e}")

    return render(request, "FreteApp/list_entregas.html", context=t_entregas)


def create_endereco(request):
    endereco_data = {
        "logradouro": request.POST.get("logradouro"),
        "cidade": request.POST.get("cidade"),
        "bairro": request.POST.get("bairro"),
        "numero": request.POST.get("numero"),
        "complemento": request.POST.get("complemento"),
        "uf": request.POST.get("uf"),
        "cep": request.POST.get("cep"),
    }

    create_cliente(request, endereco_data)


def create_cliente(request, endereco_data):
    cliente_data = {
        "endereco": Endereco.objects.create(**endereco_data),
        "nome": request.POST.get("nome"),
        "telefone": request.POST.get("telefone"),
    }

    create_entrega(request, cliente_data)


def create_entrega(request, cliente_data):
    entrega_data = {
        "cliente": Cliente.objects.create(**cliente_data),
        "pedido_numero": request.POST.get("pedido_numero"),
        "informacoes": request.POST.get("informacoes"),
        "status": request.POST.get("status"),
        "payment_pedido": request.POST.get("payment_pedido"),
        "payment_motoboy": request.POST.get("payment_motoboy"),
    }

    Entrega.objects.create(**entrega_data)
