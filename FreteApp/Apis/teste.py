import requests
from decouple import config  # Certifique-se de que você importou a biblioteca decouple


def consultar_endereco_google(end):
    endereco = end
    if not endereco:
        return {"erro": "CEP de destino inválido."}
    CHAVE = config("TOKEN_GOOGLE")
    CEP_ORIGEM = "30170-130"
    URL_GOOGLE = f"https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins={CEP_ORIGEM}&destinations={end}&key={CHAVE}"
    base_url = (
        f"https://maps.googleapis.com/maps/api/geocode/json?address={end}&key={CHAVE}"
    )
    response = requests.get(base_url)

    if response.status_code == 200:
        response_dic = response.json()
        return response_dic["results"][0]["address_components"][0]["long_name"]


print(consultar_endereco_google("rua aimores nossa senhora de fatima sabara"))
