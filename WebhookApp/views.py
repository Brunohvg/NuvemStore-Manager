import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import urllib.parse

# Create your views here.


import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def webhook_endpoint(request):
    if request.method == "POST":
        # Você pode acessar os parâmetros da query string assim:
        data = request.body

        print(data)

        # Faça o que for necessário com os parâmetros da query string
        # ...

        # Para processar o corpo do POST (se houver):

        # Faça o que for necessário com os dados JSON
        # ...

        return HttpResponse(status=200)

    return HttpResponse(status=405)  # Responde apenas a solicitações POST
