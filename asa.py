import requests
from bs4 import BeautifulSoup
import time
import webbrowser

URL_PRODUTO = "SUA_URL_AQUI"
PRECO_DESEJADO = 150.00

def verificar_preco():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "pt-BR,pt;q=0.9"
    }

    try:
        response = requests.get(URL_PRODUTO, headers=headers, timeout=15)
        if response.status_code != 200:
            return False

        soup = BeautifulSoup(response.text, 'html.parser')
        
        tag_preco = soup.find("meta", itemprop="price")
        
        if tag_preco:
            preco_atual = float(tag_preco["content"])
        else:
            elemento = soup.select_one(".andes-money-amount__fraction")
            if not elemento:
                return False
            
            texto = elemento.get_text().replace('.', '').replace(',', '.')
            preco_atual = float(texto)

        if preco_atual <= PRECO_DESEJADO:
            webbrowser.open(URL_PRODUTO)
            return True

    except:
        pass
    
    return False

while True:
    if verificar_preco():
        break
    time.sleep(1800)