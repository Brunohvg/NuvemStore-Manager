from calculador_frete import CalculadoraFrete

cal = CalculadoraFrete("30170130")

valor = cal.consultar_motoboy_google(cep_destino=34600190)

print(valor)
