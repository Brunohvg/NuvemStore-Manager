import requests
from consultar_endereco import validar_cep, consultar_endereco
from decouple import config


def consultar_valor_motoboy(cep):
    TOKEN_BORZO = config("TOKEN_BORZO")
    cep = validar_cep(cep)

    if cep:
        url_borzo = (
            "https://robotapitest-br.borzodelivery.com/api/business/1.4/calculate-order"
        )
        header = {
            "X-DV-Auth-Token": TOKEN_BORZO,
            "Content-Type": "application/json",
        }
        data = {
            "matter": "Documents",
            "points": [{"address": "30170-130"}, {"address": cep}],
        }

        try:
            response = requests.post(url_borzo, headers=header, json=data)
            response.raise_for_status()  # Lidar com erros HTTP
            response = response.json()

            valor_boy = int(float(response["order"]["payment_amount"]))

            if valor_boy <= 18:
                valor = "18.00"
                return valor

            else:
                return response["order"]["payment_amount"]

        except requests.exceptions.RequestException as e:
            # Lidar com erros de requisição, como timeouts, conexão falha, etc.
            # Pode retornar uma mensagem de erro, logar o erro, etc.
            print("Erro na requisição:", e)
            return {"erro": "Ocorreu um erro na consulta à API externa."}


print(consultar_valor_motoboy("34s600190"))
