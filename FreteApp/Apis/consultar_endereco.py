import requests


def validar_cep(cep):
    try:
        # Transforma o cep em string
        cep = str(cep)
        # Remove os espaços, . e -
        cep = cep.replace(".", "").replace("-", "").replace(" ", "")
        # Verifica se o cep digitado tem 8 digitos
        if len(cep) != 8 or not cep.isdigit():
            # Retorna o cep como invalido caso não atendas aos requesitos
            raise Exception({"Erro": f"Cep digitado é inválido:{cep}"})

        return cep
    except Exception as e:
        return None


def consultar_endereco(cep):
    status = [200, 404, 505]
    try:
        cep = validar_cep(cep)
        url = f"https://brasilaberto.com/api/v1/zipcode/{cep}"
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
