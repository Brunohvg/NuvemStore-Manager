from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .Apis.consultar_endereco import consultar_endereco
from django.contrib import messages


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

from django.contrib import messages

def _handle_end(request, data):
    if data["cep"]:
        end = consultar_endereco(data["cep"])
        if not end:
            print("CEP inválido")
            messages.add_message(request, messages.ERROR, "CEP inválido")
        return render(request, "FreteApp/cotacoes.html")

