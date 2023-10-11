import requests
import pprint
from decouple import config


def authorize():
    URL = "https://www.tiendanube.com/apps/authorize/token"
    HEADERS = {"Content-Type": "application/json"}
    DATA = {
        "client_id": "8619",
        "client_secret": "4263cfda2bc47a702f62d74784d7abcd97a237e1e5c3875b",
        "grant_type": "authorization_code",
        "code": "6bf5934bfc51eabec9ef13d5befe9efe70a4a390",
    }
    response = requests.post(URL, headers=HEADERS, json=DATA)

    return response.json()


def cliente():
    URL_CLIENTE = "https://api.nuvemshop.com.br/v1/2686287/customers?per_page=1000"

    HEADERS = {
        "Authentication": "bearer 634e1fd6d8041fd2e2fa35118e8286f6f3675546",
        "Content-Type": "application/json",
        "User-Agent": "brunovidal27.19@gmail.com",
    }
    response = requests.get(url=URL_CLIENTE, headers=HEADERS)
    data = response.json()
    return data


dados = cliente()

for dic in dados:
    print(dic)
