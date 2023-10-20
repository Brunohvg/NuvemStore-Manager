"""import requests
from decouple import config  # Certifique-se de que você importou a biblioteca decouple


def consultar_endereco_google(end):
    endereco = end
    if not endereco:
        return {"erro": "CEP de destino inválido."}
    CHAVE = config("TOKEN_GOOGLE")
    CEP_ORIGEM = "30170-130"
    URL_GOOGLE = f"https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins={CEP_ORIGEM}&destinations={end}&key={CHAVE}"

    response = requests.get(URL_GOOGLE)

    response_dict = response.json()

    return response_dict


print(consultar_endereco_google("78525-000"))
"""
import requests


def consultar_endereco(self, cep_destino):
    cep_destino_valido = self.validar_cep(cep_destino)
    if not cep_destino_valido:
        return {"erro": "CEP de destino inválido."}

    try:
        url = f"https://viacep.com.br/ws/{cep_destino_valido}/json/"
        response = requests.get(url=url)
        response.raise_for_status()

        return response.json()

    except Exception as e:
        return None


re = requests.get("https://viacep.com.br/ws/01001000/json/")
ree = re.json()
print(ree)
