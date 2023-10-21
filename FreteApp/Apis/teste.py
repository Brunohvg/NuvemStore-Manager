import requests
from decouple import config  # Certifique-se de que você importou a biblioteca decouple


def consultar_endereco_google(end):
    CHAVE = config("TOKEN_GOOGLE")
    base_url = (
        f"https://maps.googleapis.com/maps/api/geocode/json?address={end}&key={CHAVE}"
    )
    response = requests.get(base_url)

    if response.status_code == 200:
        response_dic = response.json()
        if not response_dic.get("status") == "ZERO_RESULTS":
            dados = response_dic["results"][0]["formatted_address"]
        return dados

    def buscar_endereco_googole(self, dados_destino):
        if dados_destino:
            CHAVE = config("TOKEN_GOOGLE")
            URL_GOOGLE = f"https://maps.googleapis.com/maps/api/geocode/json?address={dados_destino}&key={CHAVE}"

        try:
            response = requests.get(URL_GOOGLE)
            response.raise_for_status()

            if not response.get("status") != "ZERO_RESULTS":
                return "Erro na api"
            dados = response["results"][0]["formatted_address"]
            return dados

        except requests.exceptions.RequestException as e:
            return e
