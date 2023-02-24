import requests
import json
import time
import os

# Definindo as informações da API do Skyscanner
api_key = 'SUA_CHAVE_API_AQUI'
market = 'BR'
currency = 'BRL'
locale = 'pt-BR'

# Definindo as informações do bot do Telegram
telegram_bot_token = 'SEU_TOKEN_AQUI'
telegram_chat_id = 'SEU_CHAT_ID_AQUI'

# Define as variáveis de busca
origin = 'BSB-sky' # Brasília
destination = 'BUE-sky' # Buenos Aires
max_price = 1000

# Função para buscar voos para Buenos Aires abaixo de R$1000
def search_flights():
    url = f"https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsedates/v1.0/{market}/{currency}/{locale}/{origin}/{destination}/anytime/anytime"
    headers = {'x-rapidapi-key': api_key, 'x-rapidapi-host': 'skyscanner-skyscanner-flight-search-v1.p.rapidapi.com'}

    response = requests.get(url, headers=headers)
    data = json.loads(response.text)

    try:
        quote = data['Quotes'][0]
        price = quote['MinPrice']
        outbound_date = quote['OutboundDate']
        inbound_date = quote['InboundDate']

        if price < max_price:
            message = f"Encontrei um voo de {origin} para {destination} por {price} reais. Partida em {outbound_date} e retorno em {inbound_date}."
            send_telegram_message(message)
    except:
        pass

# Função para enviar mensagem via Telegram
def send_telegram_message(message):
    os.system(f'telegram-send --token "{telegram_bot_token}" --chat_id "{telegram_chat_id}" "{message}"')

# Loop infinito para rodar o script a cada 2 horas
while True:
    search_flights()
    time.sleep(7200) # Espera 2 horas (7200 segundos) antes de executar novamente
