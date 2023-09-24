import requests
from decouple import config


def consultar_valor_correio(cep, peso, comprimento=16, largura=12, altura=2):
    if cep:
        KEY_CORREIO = config("KEY_CORREIO")
        url_sgpweb = f"https://www.sgpweb.com.br/novo/api/consulta-precos-prazos?chave_integracao={KEY_CORREIO}"
        headers = {"Content-Type": "application/json"}
        payload = {
            "cep_origem": "30170-130",
            "cep_destino": cep,
            "peso": peso,
            "comprimento": comprimento,
            "largura": largura,
            "altura": altura,
            "servicos": ["4162", "4669"],
        }
        try:
            # Construir a URL ou payload para a consulta à API externa
            # Fazer a requisição usando requests.get() ou requests.post()
            response = requests.post(url_sgpweb, json=payload, headers=headers)
            response.raise_for_status()  # Lidar com erros HTTP

            data = response.json()

            if data[0]["Erro"] and data[1]["Erro"] == 0:
                # Processar e retornar os dados obtidos da API
                return data
            return data
        except requests.exceptions.RequestException as e:
            # Lidar com erros de requisição, como timeouts, conexão falha, etc.
            # Pode retornar uma mensagem de erro, logar o erro, etc.
            print("Erro na requisição:", e)
            return {"erro": "Ocorreu um erro na consulta à API externa."}


print(consultar_valor_correio("34600190", 2))
