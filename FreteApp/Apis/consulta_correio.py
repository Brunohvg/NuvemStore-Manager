import requests

def validar_cep(cep):
    try:
        cep = str(cep)
        cep = cep.replace(".", "").replace("-", "").replace(" ", "")
        
        if len(cep) != 8 or not cep.isdigit():
            raise Exception(f'Cep digitado é inválido: {cep}')
        
        return cep
    except Exception as e:
        return str(e)

def consultar_endereco(cep):
    status = [200, 404, 505]
    try:
        cep = validar_cep(cep)
        url = f"https://brasilaberto.com/api/v1/zipcode/{cep}"
        response = requests.get(url=url)

        if response.status_code == 200:
            data = response.json()
            return data['result']
        
        if response.status_code == 404:
            raise Exception(f'Erro:{response.status_code}: {cep}')
        
        if response.status_code == 500:
            raise Exception(f'Erro:{response.status_code}: Sistema Indisponivel no momento')

    except Exception as e:
        return str(e)

print(consultar_endereco(5555555))