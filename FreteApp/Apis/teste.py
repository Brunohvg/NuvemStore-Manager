from calculador_frete import CalculadoraFrete

cal = CalculadoraFrete("30170130")

valor = cal.consultar_valor_correio("34600190", 5, 66, 66, 66)

te = cal.consultar_valor_motoboy("34600190")


def converter(valor):
    valor = valor.replace(",", ".")
    valor = float(valor)
    return valor


print(type(te))
