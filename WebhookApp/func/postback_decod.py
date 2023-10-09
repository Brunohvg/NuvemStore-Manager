def decodificar_dados_postback(data):
    import urllib.parse

    """
    Decodifica os dados do postback em um dicionário.

    Args:
        data: Os dados do postback no formato de query string.

    Returns:
        Um dicionário com os dados do postback decodificados.
    """

    data_json = urllib.parse.parse_qs(data.decode("utf-8"))
    return data_json
