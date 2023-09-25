from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .Apis.calculador_frete import CalculadoraFrete
from django.contrib import messages


@login_required
def dashboard(request):
    return render(request, "FreteApp/dashboard.html")


@login_required
def calculadora(request):
    active_menu = "calculadora"
    if request.method == "POST":
        return _handle_post(request)
    else:
        return render(request, "FreteApp/cotacoes.html", {"active_menu": active_menu})


@login_required
def _handle_post(request):
    handle_request = {
        "cep": request.POST.get("cep"),
        "comprimento": request.POST.get("comprimento"),
        "largura": request.POST.get("largura"),
        "altura": request.POST.get("altura"),
        "peso": request.POST.get("peso"),
    }
    if handle_request:
        data = handle_request
        return _handle_end(request, data)


@login_required
def _handle_end(request, data):
    calculadora = CalculadoraFrete("30170130")
    cep = data["cep"]
    if cep:
        endereco = calculadora.consultar_endereco(cep)
        if not endereco:
            messages.add_message(
                request, messages.ERROR, f"Atenção o cep: {cep} é invalido"
            )
        else:
            end_request = {
                "rua": endereco["street"],
                "bairro": endereco["district"],
                "cidade": endereco["city"],
                "uf": endereco["stateShortname"],
                "cep": endereco["zipcode"],
                "complemento": endereco["complement"],
            }
            return _handle_valor_correio(request, data, end_request)
            # return render(request, "FreteApp/cotacoes.html", context=end_request)
        return render(request, "FreteApp/cotacoes.html")


def _handle_valor_correio(request, data, end_request):
    calculadora = CalculadoraFrete("30170130")
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

        correio_request = {
            "valor_sedex": dados_sedex["Valor"],
            "prazo_sedex": dados_sedex["PrazoEntrega"],
            "valor_pac": dados_pac["Valor"],
            "prazo_pac": dados_pac["PrazoEntrega"],
        }

        return _handle_valor_motoboy(request, data, end_request, correio_request)

    except ValueError as e:
        error_message = str(e)  # Mensagem de erro da exceção
        messages.add_message(
            request,
            messages.ERROR,
            f"{error_message} => Soma dos 3 não pode ultrapassar 200 cm ",
        )
        return render(request, "FreteApp/cotacoes.html")


def _handle_valor_motoboy(request, data, end_request, correio_request):
    calculador = CalculadoraFrete("30170130")
    cep = data["cep"]
    if cep:
        valor_motoboy = calculador.consultar_valor_motoboy(cep)
        motoboy_request = {"valor_motoboy": valor_motoboy}

        return render(
            request,
            "FreteApp/cotacoes.html",
            context={**correio_request, **end_request, **motoboy_request},
        )
    return render(
        request,
        "FreteApp/cotacoes.html",
        context={
            **correio_request,
            **end_request,
        },
    )
