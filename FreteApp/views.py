from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .Apis.consultar_endereco import consultar_endereco
import json


from django.http import HttpResponse


@login_required
def dashboard(request, data):
    if request.method == "POST":
        print(data["cep"])
        return render(request, "FreteApp/cotacoes.html")


@login_required
def base(request):
    if request.method == "POST":
        return _handle_post(request)
    else:
        return render(request, "FreteApp/cotacoes.html")


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


def _handle_end(request, data):
    if request.method == "POST":
        try:
            cep = data["cep"]
            # Verifique se o campo "cep" não está vazio ou nulo
            if not cep:
                return render(
                    request,
                    "FreteApp/cotacoes.html",
                    {"error_message": "O campo CEP não pode estar vazio."},
                )

            # Consultar o endereço com base no CEP
            try:
                end = consultar_endereco(cep)
                print(end)
            except KeyError:
                return render(
                    request,
                    "FreteApp/cotacoes.html",
                    {"error_message": "Erro ao consultar o endereço."},
                )

            # Continuar com o processamento
            return render(request, "FreteApp/cotacoes.html")

        except KeyError:
            return render(
                request,
                "FreteApp/cotacoes.html",
                {"error_message": "Erro no processamento do formulário."},
            )
    else:
        return render(request, "FreteApp/cotacoes.html")
