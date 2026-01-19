
from flask import Flask
import requests

app = Flask(__name__)

# --- CONFIGURAÇÃO ---
LINK_BINANCE = "https://www.binance.com/referral/earn-together/refer2earn-usdc/claim?hl=pt&ref=GRO_28502_9GMCA&utm_source=default"
LINK_BYBIT = "COLA_AQUI_O_TEU_LINK_BYBIT"

@app.route('/')
def home():
    try:
        url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        preco = float(requests.get(url).json()['price'])
        preco_formatado = f"{preco:,.2f}"
    except:
        preco_formatado = "A carregar..."

    return f"""
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {{ font-family: 'Segoe UI', sans-serif; background: #0b0e11; color: white; text-align: center; padding: 20px; }}
           .card {{ background: #1e2329; border-radius: 20px; padding: 30px; border: 1px solid #ffb11a; display: inline-block; margin-top: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }}
           .price {{ font-size: 3em; color: #ffb11a; font-weight: bold; }}
           .btn {{ display: block; padding: 20px; margin: 15px 0; border-radius: 12px; text-decoration: none; font-weight: bold; font-size: 1.2em; transition: 0.3s; }}
           .binance {{ background: #f3ba2f; color: black; }}
           .bybit {{ background: #000000; color: white; border: 2px solid #ffb11a; }}
           .tag {{ background: #2b3139; padding: 5px 15px; border-radius: 50px; font-size: 0.8em; color: #848e9c; }}
        </style>
    </head>
    <body>
        <div class="tag">IA SIGNAL BOT Ativo</div>
        <h1>MERCADO EM TEMPO REAL</h1>
        <div class="card">
            <p>Bitcoin (BTC/USDT)</p>
            <div class="price">${preco_formatado}</div>
            <p style="color: #0ecb81; font-weight: bold;">⚡ SINAL: OPORTUNIDADE DETETADA</p>
        </div>
        
        <h3>Regista-te para copiar o sinal:</h3>
        <a href="{LINK_BINANCE}" class="btn binance">REIVINDICAR BÓNUS BINANCE</a>
        <a href="{LINK_BYBIT}" class="btn bybit">REIVINDICAR BÓNUS BYBIT</a>
        
        <p style="font-size: 0.7em; color: gray; margin-top: 50px;">Monitorização em tempo real via API oficial.</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
