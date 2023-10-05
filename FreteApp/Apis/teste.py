from calculador_frete import CalculadoraFrete

cal = CalculadoraFrete("34600190")

valor = cal.buscar_endereco_googole("35384000")


import re

lista = valor["destination_addresses"]

# Use uma expressão regular para encontrar o padrão do CEP (5 dígitos, hífen e mais 3 dígitos)
padrao_cep = r"\b\d{5}-\d{3}\b"

# Inicialize uma lista para armazenar os CEPs encontrados
ceps_encontrados = []

# Itere pelos elementos da lista
for texto in lista:
    resultado = re.search(padrao_cep, texto)
    if resultado:
        cep_encontrado = resultado.group()
        ceps_encontrados.append(cep_encontrado)

# Imprima os CEPs encontrados
if ceps_encontrados:
    print("CEPs encontrados na lista:")
    for cep in ceps_encontrados:
        print(cep)
else:
    print("Nenhum CEP encontrado na lista.")
