from .func.postback_decod import decodificar_dados_postback
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Create your views here.


@csrf_exempt
@require_POST
def webhook_endpoint(request):
    # Obtém os dados do postback da query string
    data = request.body

    # Decodifica os dados do postback

    data_json = decodificar_dados_postback(data)

    # Processa os dados do postback
    print(data_json.get("old_status"))
    print(data_json.get("desired_status"))
    # Retorne uma resposta
    return HttpResponse(status=200)
