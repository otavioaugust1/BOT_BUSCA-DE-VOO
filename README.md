# Script de busca de voos Brasilia-BR para Buenos Aires-AR

![Badge em Desenvolvimento](https://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)

![GitHub Org's stars](https://img.shields.io/github/stars/camilafernanda?style=social)


Este script Python busca voos de Brasília para Buenos Aires abaixo de R$1000 na API do Skyscanner e envia uma mensagem para o seu celular via Telegram caso encontre algum voo disponível. Ele é executado a cada 2 horas.

## 🛠️ Pré-requisitos
Antes de executar este script, você precisa ter acesso à API do Skyscanner e ao bot do Telegram. Para obter as chaves de acesso necessárias, siga as instruções abaixo:

### 🛠️ API do Skyscanner
1. Acesse o site do Skyscanner Developers
2. Crie uma conta (se ainda não tiver uma)
3. Crie um novo aplicativo e obtenha sua chave de API

### 🛠️ Bot do Telegram
1. Abra o aplicativo do Telegram
2. Busque por "BotFather"
3. Inicie uma conversa com o BotFather e siga as instruções para criar um novo bot
4. Anote o token do bot gerado pelo BotFather
5. Envie uma mensagem para o seu bot e acesse a URL https://api.telegram.org/bot<seu_token_aqui>/getUpdates
6. Procure pelo valor do atributo chat_id e anote-o


## 🛠️ Instalação
1. Clone este repositório ou faça o download do código fonte
2. Abra o terminal e navegue até o diretório onde o script foi salvo
3. Instale as dependências necessárias:

```
pip install requests
pip install python-telegram-bot
pip install python-telegram-send
```
4. Abra o arquivo busca_passagens.py em um editor de texto
5. Substitua "SUA_CHAVE_API_AQUI", "SEU_TOKEN_AQUI" e "SEU_CHAT_ID_AQUI" pelas suas informações de acesso à API do Skyscanner e ao bot do Telegram
6. Salve as alterações no arquivo


## 🛠️ Execução
Para executar o script, abra o terminal e navegue até o diretório onde o script foi salvo. Em seguida, digite o seguinte comando:
```
python busca_passagens.py
```
O script será executado e buscará voos de Brasília para Buenos Aires abaixo de R$1000 a cada 2 horas. Caso encontre um voo disponível, o script enviará uma mensagem para o seu celular via Telegram.

Você pode interromper a execução do script a qualquer momento pressionando Ctrl + C no terminal.

## 🛠️ Limitações
Observe que este script faz uma busca por voos dentro de um período de 4 meses a partir da data atual. Se você deseja procurar voos em um período diferente, será necessário ajustar as variáveis `start_date` e `end_date no arquivo` `flight_alert.py`.

## 🛠️ Licença
Este script é distribuído sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.