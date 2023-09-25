import requests
from decouple import config  # Certifique-se de que você importou a biblioteca decouple


class CalculadoraFrete:
    def __init__(self, cep_origem):
        self.cep_origem = cep_origem

    def validar_cep(self, cep):
        try:
            # Transforma o cep em string
            cep = str(cep)
            # Remove os espaços, . e -
            cep = cep.replace(".", "").replace("-", "").replace(" ", "")
            # Verifica se o cep digitado tem 8 dígitos
            if len(cep) != 8 or not cep.isdigit():
                # Retorna o cep como inválido caso não atenda aos requisitos
                raise ValueError(f"Cep digitado é inválido: {cep}")

            return cep
        except ValueError as e:
            return None

    def consultar_endereco(self, cep_destino):
        cep_destino_valido = self.validar_cep(cep_destino)
        if not cep_destino_valido:
            return {"erro": "CEP de destino inválido."}

        try:
            url = f"https://brasilaberto.com/api/v1/zipcode/{cep_destino_valido}"
            response = requests.get(url=url)

            if response.status_code == 200:
                data = response.json()
                return data["result"]

            if response.status_code == 404:
                raise Exception({"Erro": 400})

            if response.status_code == 500:
                raise Exception(
                    f"Erro:{response.status_code}: Sistema Indisponivel no momento"
                )

        except Exception as e:
            return None

    def consultar_valor_correio(self, cep_destino, peso, comprimento, largura, altura):
        # Valida o CEP de destino antes de prosseguir
        cep_destino_valido = self.validar_cep(cep_destino)
        if not cep_destino_valido:
            return {"erro": "CEP de destino inválido."}
        # Imprimir os valores de altura e largura
        # print(f"Altura: {altura}, Largura: {largura}")
        KEY_CORREIO = config("KEY_CORREIO")
        url_sgpweb = f"https://www.sgpweb.com.br/novo/api/consulta-precos-prazos?chave_integracao={KEY_CORREIO}"
        headers = {"Content-Type": "application/json"}
        payload = {
            "cep_origem": self.cep_origem,
            "cep_destino": cep_destino_valido,
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

    def consultar_valor_motoboy(self, cep_destino):
        # Valida o CEP de destino antes de prosseguir
        cep_destino_valido = self.validar_cep(cep_destino)
        if not cep_destino_valido:
            return {"erro": "CEP de destino inválido."}

        TOKEN_BORZO = config("TOKEN_BORZO")
        url_borzo = (
            "https://robotapitest-br.borzodelivery.com/api/business/1.4/calculate-order"
        )
        header = {
            "X-DV-Auth-Token": TOKEN_BORZO,
            "Content-Type": "application/json",
        }
        data = {
            "matter": "Documents",
            "points": [{"address": self.cep_origem}, {"address": cep_destino_valido}],
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


"""# Exemplo de uso
calculadora = CalculadoraFrete('30170130')
cep_destino = "34600190"
peso = 1
comprimento = 50
largura = 30
altura = 22

# Valida o CEP de destino antes de fazer a consulta do valor do motoboy
cep_destino_valido = calculadora.validar_cep(cep_destino)
if cep_destino_valido:
    resultado_correio = calculadora.consultar_valor_correio(
        cep_destino_valido, peso, comprimento, largura, altura
    )
    print("Resultado do Correio:", resultado_correio)

    resultado_motoboy = calculadora.consultar_valor_motoboy(cep_destino_valido)
    print("Resultado do Motoboy:", resultado_motoboy)
else:
    print("CEP de destino inválido.")
"""
