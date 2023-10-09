import requests

url = "https://api.pagar.me/1/payment_links"

payload = {
    "api_key": "ak_test_FD0mK5HaoZCtxQrMtbmJl9NTwtwYEU",
    "amount": 20000,
    "name": "Novo Link",
    "items": [
        {
            "id": "1",
            "title": "Novo Link",
            "unit_price": 20000,
            "quantity": 1,
            "tangible": True,
        }
    ],
    "postback_config": {
        "orders": "https://843b-2804-1b3-61c0-fc1a-edf7-baad-49db-b844.ngrok-free.app/webhook/",
        "transactions": "https://843b-2804-1b3-61c0-fc1a-edf7-baad-49db-b844.ngrok-free.app/webhook/",
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

# TODO dados com ordem e transacioes
"""
{
'id':[
'or_clng5lgr00q4l019tqu3essov'
],
'fingerprint':[
'5ee45733ccc8a102377f5a26959644435e58b831'
],
'event':[
'order_status_changed'
],
'old_status':[
'created'
],
'desired_status':[
'paid'
],
'current_status':[
'paid'
],
'object':[
'order'
],
'order[object]':[
'order'
],
'order[id]':[
'or_clng5lgr00q4l019tqu3essov'
],
'order[company_id]':[
'5c82ce84615db3320f265071'
],
'order[status]':[
'paid'
],
'order[amount]':[
'20000'
],
'order[items][0][object]':[
'item'
],
'order[items][0][id]':[
'1'
],
'order[items][0][title]':[
'Novo Link'
],
'order[items][0][unit_price]':[
'20000'
],
'order[items][0][quantity]':[
'1'
],
'order[items][0][tangible]':[
'true'
],
'order[payment_link_id]':[
'pl_clng5laxl0q4i019t10pr8jrc'
],
'order[postback_url]':[
'https://843b-2804-1b3-61c0-fc1a-edf7-baad-49db-b844.ngrok-free.app/webhook/'
],
'order[date_created]':[
'2023-10-07T14:51:38.124Z'
]
}[07/Oct/2023 11:52:00] "POST /webhook/ HTTP/1.1" 200 30 {'id': ['2200568617'], 'fingerprint': ['ad0f9adf65e7fdf629ec9b5d3eef49e64e16e9ea'], 'event': ['transaction_status_changed'], 'old_status': ['processing'], 'desired_status': ['paid'], 'current_status': ['paid'], 'object': ['transaction'], 'transaction[object]': ['transaction'], 'transaction[status]': ['paid'], 'transaction[status_reason]': ['acquirer'], 'transaction[acquirer_response_code]': ['0000'], 'transaction[acquirer_response_message]': ['Transação aprovada com sucesso'], 'transaction[acquirer_name]': ['pagarme'], 'transaction[acquirer_id]': ['5c82ce84615db3320f265072'], 'transaction[authorization_code]': ['636973'], 'transaction[tid]': ['2200568617'], 'transaction[nsu]': ['2200568617'], 'transaction[date_created]': ['2023-10-07T14:52:01.708Z'], 'transaction[date_updated]': ['2023-10-07T14:52:02.073Z'], 'transaction[amount]': ['35000'], 'transaction[authorized_amount]': ['35000'], 'transaction[paid_amount]': ['35000'], 'transaction[refunded_amount]': ['0'], 'transaction[installments]': ['3'], 'transaction[id]': ['2200568617'], 'transaction[cost]': ['120'], 'transaction[card_holder_name]': ['as'], 'transaction[card_last_digits]': ['0010'], 'transaction[card_first_digits]': ['400000'], 'transaction[card_brand]': ['visa'], 'transaction[card_magstripe_fallback]': ['false'], 'transaction[card_funding_source]': ['Credit'], 'transaction[cvm_pin]': ['false'], 'transaction[postback_url]': ['https://843b-2804-1b3-61c0-fc1a-edf7-baad-49db-b844.ngrok-free.app/webhook/'], 'transaction[payment_method]': ['credit_card'], 'transaction[capture_method]': ['ecommerce'], 'transaction[boleto_expiration_date]': ['2023-10-27T03:00:00.000Z'], 'transaction[referer]': ['encryption_key'], 'transaction[ip]': ['2804:1b3:61c0:fc1a:edf7:baad:49db:b844'], 'transaction[customer][object]': ['customer'], 'transaction[customer][id]': ['15586564'], 'transaction[customer][external_id]': ['brunohenrique27.19@gmail.com'], 'transaction[customer][type]': ['individual'], 'transaction[customer][country]': ['br'], 'transaction[customer][document_type]': ['cpf'], 'transaction[customer][name]': ['Bruno'], 'transaction[customer][email]': ['brunohenrique27.19@gmail.com'], 'transaction[customer][phone_numbers][0]': ['+5531999999999'], 'transaction[customer][date_created]': ['2023-10-07T14:52:01.640Z'], 'transaction[customer][documents][0][object]': ['document'], 'transaction[customer][documents][0][id]': ['doc_clng5lywi0ovb019tuztn0owp'], 'transaction[customer][documents][0][type]': ['cpf'], 'transaction[customer][documents][0][number]': ['10009142673'], 'transaction[billing][object]': ['billing'], 'transaction[billing][id]': ['6369223'], 'transaction[billing][name]': ['Bruno'], 'transaction[billing][address][object]': ['address'], 'transaction[billing][address][street]': ['Rua São Paulo'], 'transaction[billing][address][complementary]': ['Sem complemento'], 'transaction[billing][address][street_number]': ['2'], 'transaction[billing][address][neighborhood]': ['Centro'], 'transaction[billing][address][city]': ['Belo Horizonte'], 'transaction[billing][address][state]': ['MG'], 'transaction[billing][address][zipcode]': ['30170130'], 'transaction[billing][address][country]': ['br'], 'transaction[billing][address][id]': ['11352793'], 'transaction[card][object]': ['card'], 'transaction[card][id]': ['card_clng5lyxq0ovc019tgk87kbj1'], 'transaction[card][date_created]': ['2023-10-07T14:52:01.694Z'], 'transaction[card][date_updated]': ['2023-10-07T14:52:01.694Z'], 'transaction[card][brand]': ['visa'], 'transaction[card][holder_name]': ['as'], 'transaction[card][first_digits]': ['400000'], 'transaction[card][last_digits]': ['0010'], 'transaction[card][country]': ['UNITED STATES'], 'transaction[card][fingerprint]': ['cj94fhdxk0afq0j99lwshbcbu'], 'transaction[card][expiration_date]': ['1026'], 'transaction[device][session]': ['f1200aa1287ebefa68573562b73177ee85b276b5'], 'transaction[fraud_covered]': ['false'], 'transaction[order_id]': ['or_clng5lgr00q4l019tqu3essov'], 'transaction[risk_level]': ['very_low']} [07/Oct/2023 11:52:00] "POST /webhook/ HTTP/1.1" 200 30 {'id': ['2200568589'], 'fingerprint': ['d869f69419ffbe32a7c08fcf17fbcb75a515ff63'], 'event': ['transaction_status_changed'], 'old_status': ['processing'], 'desired_status': ['paid'], 'current_status': ['paid'], 'object': ['transaction'], 'transaction[object]': ['transaction'], 'transaction[status]': ['paid'], 'transaction[status_reason]': ['acquirer'], 'transaction[acquirer_response_code]': ['0000'], 'transaction[acquirer_response_message]': ['Transação aprovada com sucesso'], 'transaction[acquirer_name]': ['pagarme'], 'transaction[acquirer_id]': ['5c82ce84615db3320f265072'], 'transaction[authorization_code]': ['57404'], 'transaction[tid]': ['2200568589'], 'transaction[nsu]': ['2200568589'], 'transaction[date_created]': ['2023-10-07T14:38:58.605Z'], 'transaction[date_updated]': ['2023-10-07T14:38:58.855Z'], 'transaction[amount]': ['30000'], 'transaction[authorized_amount]': ['30000'], 'transaction[paid_amount]': ['30000'], 'transaction[refunded_amount]': ['0'], 'transaction[installments]': ['2'], 'transaction[id]': ['2200568589'], 'transaction[cost]': ['120'], 'transaction[card_holder_name]': ['a'], 'transaction[card_last_digits]': ['0010'], 'transaction[card_first_digits]': ['400000'], 'transaction[card_brand]': ['visa'], 'transaction[card_magstripe_fallback]': ['false'], 'transaction[card_funding_source]': ['Credit'], 'transaction[cvm_pin]': ['false'], 'transaction[postback_url]': ['https://843b-2804-1b3-61c0-fc1a-edf7-baad-49db-b844.ngrok-free.app/webhook/'], 'transaction[payment_method]': ['credit_card'], 'transaction[capture_method]': ['ecommerce'], 'transaction[boleto_expiration_date]': ['2023-10-27T03:00:00.000Z'], 'transaction[referer]': ['encryption_key'], 'transaction[ip]': ['2804:1b3:61c0:fc1a:edf7:baad:49db:b844'], 'transaction[customer][object]': ['customer'], 'transaction[customer][id]': ['15586451'], 'transaction[customer][external_id]': ['teste@teste.com.br'], 'transaction[customer][type]': ['individual'], 'transaction[customer][country]': ['br'], 'transaction[customer][document_type]': ['cpf'], 'transaction[customer][name]': ['Maria da conceicao gomes custodio'], 'transaction[customer][email]': ['teste@teste.com.br'], 'transaction[customer][phone_numbers][0]': ['+5531973121254'], 'transaction[customer][date_created]': ['2023-10-07T14:38:58.564Z'], 'transaction[customer][documents][0][object]': ['document'], 'transaction[customer][documents][0][id]': ['doc_clng556ob0p94019tetjv36hf'], 'transaction[customer][documents][0][type]': ['cpf'], 'transaction[customer][documents][0][number]': ['10009142673'], 'transaction[billing][object]': ['billing'], 'transaction[billing][id]': ['6369219'], 'transaction[billing][name]': ['Maria da conceicao gomes custodio'], 'transaction[billing][address][object]': ['address'], 'transaction[billing][address][street]': ['Rua São Paulo'], 'transaction[billing][address][complementary]': ['Sem complemento'], 'transaction[billing][address][street_number]': ['1'], 'transaction[billing][address][neighborhood]': ['Centro'], 'transaction[billing][address][city]': ['Belo Horizonte'], 'transaction[billing][address][state]': ['MG'], 'transaction[billing][address][zipcode]': ['30170130'], 'transaction[billing][address][country]': ['br'], 'transaction[billing][address][id]': ['11352680'], 'transaction[card][object]': ['card'], 'transaction[card][id]': ['card_clng556p20p95019th75flew4'], 'transaction[card][date_created]': ['2023-10-07T14:38:58.598Z'], 'transaction[card][date_updated]': ['2023-10-07T14:38:58.598Z'], 'transaction[card][brand]': ['visa'], 'transaction[card][holder_name]': ['a'], 'transaction[card][first_digits]': ['400000'], 'transaction[card][last_digits]': ['0010'], 'transaction[card][country]': ['UNITED STATES'], 'transaction[card][fingerprint]': ['cj94fhdxk0afq0j99lwshbcbu'], 'transaction[card][expiration_date]': ['1026'], 'transaction[device][session]': ['f1200aa1287ebefa68573562b73177ee85b276b5'], 'transaction[fraud_covered]': ['false'], 'transaction[order_id]': ['or_clng54ms20otz019tutud5o37'], 'transaction[risk_level]': ['very_low']} [07/Oct/2023 11:52:08] "POST /webhook/ HTTP/1.1" 200 30 {'id': ['or_clng54ms20otz019tutud5o37'], 'fingerprint': ['0e31424ef1952c2c00da5470f9888c0abec08b09'], 'event': ['order_status_changed'], 'old_status': ['created'], 'desired_status': ['paid'], 'current_status': ['paid'], 'object': ['order'], 'order[object]': ['order'], 'order[id]': ['or_clng54ms20otz019tutud5o37'], 'order[company_id]': ['5c82ce84615db3320f265071'], 'order[status]': ['paid'], 'order[amount]': ['20000'], 'order[items][0][object]': ['item'], 'order[items][0][id]': ['1'], 'order[items][0][title]': ['Novo Link'], 'order[items][0][unit_price]': ['20000'], 'order[items][0][quantity]': ['1'], 'order[items][0][tangible]': ['true'], 'order[payment_link_id]': ['pl_clng4zb3m0q2e019tuc7i0nob'], 'order[postback_url]': ['https://843b-2804-1b3-61c0-fc1a-edf7-baad-49db-b844.ngrok-free.app/webhook/'], 'order[date_created]': ['2023-10-07T14:38:32.786Z']} [07/Oct/2023 11:52:08] "POST /webhook/ HTTP/1.1" 200 30 {'id': ['2200568609'], 'fingerprint': ['3661e640132902f368df2e72efc3023524c414eb'], 'event': ['transaction_status_changed'], 'old_status': ['processing'], 'desired_status': ['paid'], 'current_status': ['paid'], 'object': ['transaction'], 'transaction[object]': ['transaction'], 'transaction[status]': ['paid'], 'transaction[status_reason]': ['acquirer'], 'transaction[acquirer_response_code]': ['0000'], 'transaction[acquirer_response_message]': ['Transação aprovada com sucesso'], 'transaction[acquirer_name]': ['pagarme'], 'transaction[acquirer_id]': ['5c82ce84615db3320f265072'], 'transaction[authorization_code]': ['58032'], 'transaction[tid]': ['2200568609'], 'transaction[nsu]': ['2200568609'], 'transaction[date_created]': ['2023-10-07T14:47:42.682Z'], 'transaction[date_updated]': ['2023-10-07T14:47:42.990Z'], 'transaction[amount]': ['35000'], 'transaction[authorized_amount]': ['35000'], 'transaction[paid_amount]': ['35000'], 'transaction[refunded_amount]': ['0'], 'transaction[installments]': ['3'], 'transaction[id]': ['2200568609'], 'transaction[cost]': ['120'], 'transaction[card_holder_name]': ['dasda'], 'transaction[card_last_digits]': ['0010'], 'transaction[card_first_digits]': ['400000'], 'transaction[card_brand]': ['visa'], 'transaction[card_magstripe_fallback]': ['false'], 'transaction[card_funding_source]': ['Credit'], 'transaction[cvm_pin]': ['false'], 'transaction[postback_url]': ['https://843b-2804-1b3-61c0-fc1a-edf7-baad-49db-b844.ngrok-free.app/webhook/'], 'transaction[payment_method]': ['credit_card'], 'transaction[capture_method]': ['ecommerce'], 'transaction[boleto_expiration_date]': ['2023-10-27T03:00:00.000Z'], 'transaction[referer]': ['encryption_key'], 'transaction[ip]': ['2804:1b3:61c0:fc1a:edf7:baad:49db:b844'], 'transaction[customer][object]': ['customer'], 'transaction[customer][id]': ['15586538'], 'transaction[customer][external_id]': ['brunohenrique27.19@gmail.com'], 'transaction[customer][type]': ['individual'], 'transaction[customer][country]': ['br'], 'transaction[customer][document_type]': ['cpf'], 'transaction[customer][name]': ['Bruno'], 'transaction[customer][email]': ['brunohenrique27.19@gmail.com'], 'transaction[customer][phone_numbers][0]': ['+5531973121456'], 'transaction[customer][date_created]': ['2023-10-07T14:47:42.631Z'], 'transaction[customer][documents][0][object]': ['document'], 'transaction[customer][documents][0][id]': ['doc_clng5gf1r0q45019tc2rctaah'], 'transaction[customer][documents][0][type]': ['cpf'], 'transaction[customer][documents][0][number]': ['10009142673'], 'transaction[billing][object]': ['billing'], 'transaction[billing][id]': ['6369222'], 'transaction[billing][name]': ['Bruno'], 'transaction[billing][address][object]': ['address'], 'transaction[billing][address][street]': ['Rua São Paulo'], 'transaction[billing][address][complementary]': ['Sem complemento'], 'transaction[billing][address][street_number]': ['1'], 'transaction[billing][address][neighborhood]': ['Centro'], 'transaction[billing][address][city]': ['Belo Horizonte'], 'transaction[billing][address][state]': ['MG'], 'transaction[billing][address][zipcode]': ['30170130'], 'transaction[billing][address][country]': ['br'], 'transaction[billing][address][id]': ['11352767'], 'transaction[card][object]': ['card'], 'transaction[card][id]': ['card_clng5gf2q0q46019tazuvep0x'], 'transaction[card][date_created]': ['2023-10-07T14:47:42.675Z'], 'transaction[card][date_updated]': ['2023-10-07T14:47:42.675Z'], 'transaction[card][brand]': ['visa'], 'transaction[card][holder_name]': ['dasda'], 'transaction[card][first_digits]': ['400000'], 'transaction[card][last_digits]': ['0010'], 'transaction[card][country]': ['UNITED STATES'], 'transaction[card][fingerprint]': ['cj94fhdxk0afq0j99lwshbcbu'], 'transaction[card][expiration_date]': ['1026'], 'transaction[device][session]': ['f1200aa1287ebefa68573562b73177ee85b276b5'], 'transaction[fraud_covered]': ['false'], 'transaction[order_id]': ['or_clng5fv7b0piw019tgzkk27cu'], 'transaction[risk_level]': ['very_low']} """

# TODO DADOS SOMENTE COM O TRANSACIOES

"""
{
'id':[
'2200568661'
],
'fingerprint':[
'4a1b3192f63e8589b1fe2a7ee8a4b8468d09e7ae'
],
'event':[
'transaction_status_changed'
],
'old_status':[
'processing'
],
'desired_status':[
'paid'
],
'current_status':[
'paid'
],
'object':[
'transaction'
],
'transaction[object]':[
'transaction'
],
'transaction[status]':[
'paid'
],
'transaction[status_reason]':[
'acquirer'
],
'transaction[acquirer_response_code]':[
'0000'
],
'transaction[acquirer_response_message]':[
'Transação aprovada com sucesso'
],
'transaction[acquirer_name]':[
'pagarme'
],
'transaction[acquirer_id]':[
'5c82ce84615db3320f265072'
],
'transaction[authorization_code]':[
'11724'
],
'transaction[tid]':[
'2200568661'
],
'transaction[nsu]':[
'2200568661'
],
'transaction[date_created]':[
'2023-10-07T15:14:43.571Z'
],
'transaction[date_updated]':[
'2023-10-07T15:14:43.923Z'
],
'transaction[amount]':[
'35000'
],
'transaction[authorized_amount]':[
'35000'
],
'transaction[paid_amount]':[
'35000'
],
'transaction[refunded_amount]':[
'0'
],
'transaction[installments]':[
'3'
],
'transaction[id]':[
'2200568661'
],
'transaction[cost]':[
'120'
],
'transaction[card_holder_name]':[
'aBrunoa'
],
'transaction[card_last_digits]':[
'0010'
],
'transaction[card_first_digits]':[
'400000'
],
'transaction[card_brand]':[
'visa'
],
'transaction[card_magstripe_fallback]':[
'false'
],
'transaction[card_funding_source]':[
'Credit'
],
'transaction[cvm_pin]':[
'false'
],
'transaction[postback_url]':[
'https://843b-2804-1b3-61c0-fc1a-edf7-baad-49db-b844.ngrok-free.app/webhook/'
],
'transaction[payment_method]':[
'credit_card'
],
'transaction[capture_method]':[
'ecommerce'
],
'transaction[boleto_expiration_date]':[
'2023-10-27T03:00:00.000Z'
],
'transaction[referer]':[
'encryption_key'
],
'transaction[ip]':[
'2804:1b3:61c0:fc1a:edf7:baad:49db:b844'
],
'transaction[customer][object]':[
'customer'
],
'transaction[customer][id]':[
'15586684'
],
'transaction[customer][external_id]':[
'brunohenrique27.19@gmail.com'
],
'transaction[customer][type]':[
'individual'
],
'transaction[customer][country]':[
'br'
],
'transaction[customer][document_type]':[
'cpf'
],
'transaction[customer][name]':[
'Bruno'
],
'transaction[customer][email]':[
'brunohenrique27.19@gmail.com'
],
'transaction[customer][phone_numbers][0]':[
'+5531973121650'
],
'transaction[customer][date_created]':[
'2023-10-07T15:14:43.530Z'
],
'transaction[customer][documents][0][object]':[
'document'
],
'transaction[customer][documents][0][id]':[
'doc_clng6f5qp0pbj019t3tqrkfom'
],
'transaction[customer][documents][0][type]':[
'cpf'
],
'transaction[customer][documents][0][number]':[
'10009142673'
],
'transaction[billing][object]':[
'billing'
],
'transaction[billing][id]':[
'6369225'
],
'transaction[billing][name]':[
'Bruno'
],
'transaction[billing][address][object]':[
'address'
],
'transaction[billing][address][street]':[
'Rua Aimorés'
],
'transaction[billing][address][complementary]':[
'Sem complemento'
],
'transaction[billing][address][street_number]':[
'22'
],
'transaction[billing][address][neighborhood]':[
'Nossa Senhora de Fátima'
],
'transaction[billing][address][city]':[
'Sabará'
],
'transaction[billing][address][state]':[
'MG'
],
'transaction[billing][address][zipcode]':[
'34600190'
],
'transaction[billing][address][country]':[
'br'
],
'transaction[billing][address][id]':[
'11352913'
],
'transaction[card][object]':[
'card'
],
'transaction[card][id]':[
'card_clng6f5rf0pbk019tsx7cnn53'
],
'transaction[card][date_created]':[
'2023-10-07T15:14:43.563Z'
],
'transaction[card][date_updated]':[
'2023-10-07T15:14:43.563Z'
],
'transaction[card][brand]':[
'visa'
],
'transaction[card][holder_name]':[
'aBrunoa'
],
'transaction[card][first_digits]':[
'400000'
],
'transaction[card][last_digits]':[
'0010'
],
'transaction[card][country]':[
'UNITED STATES'
],
'transaction[card][fingerprint]':[
'cj94fhdxk0afq0j99lwshbcbu'
],
'transaction[card][expiration_date]':[
'1026'
],
'transaction[device][session]':[
'f1200aa1287ebefa68573562b73177ee85b276b5'
],
'transaction[fraud_covered]':[
'false'
],
'transaction[order_id]':[
'or_clng6egx60pbg019tx1kj64ec'
],
'transaction[risk_level]':[
'very_low'
]
}
"""
