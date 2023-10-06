import requests

url = "https://api.pagar.me/1/payment_links"

payload = {
    "api_key": "ak_test_FD0mK5HaoZCtxQrMtbmJl9NTwtwYEU",
    "amount": 20000,
    "name": "Brsuno",
    "items": [
        {
            "id": "1",
            "title": "Brsuno",
            "unit_price": 20000,
            "quantity": 1,
            "tangible": True,
        }
    ],
    "postback_config": {
        "orders": "https://a316-2804-1b3-61c0-fc1a-1944-ad9c-c548-f323.ngrok-free.app/webhook/",
        "transactions": "https://a316-2804-1b3-61c0-fc1a-1944-ad9c-c548-f323.ngrok-free.app/webhook/",
    },
    "payment_config": {
        "boleto": {"enabled": False, "expires_in": 20},
        "credit_card": {
            "enabled": True,
            "free_installments": 1,
            "interest_rate": 25,
            "max_installments": 3,
        },
        "default_payment_method": "boleto",
    },
    "max_orders": 3,
    "expires_in": 300,
}
headers = {"accept": "application/json", "content-type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
