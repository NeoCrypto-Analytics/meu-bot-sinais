from flask import Flask
import requests

app = Flask(__name__)

# --- CONFIGURAÇÃO ---
# Quando a Bybit te aprovar, vais colar o teu link aqui:
LINK_BYBIT = "https://www.bybit.com/pt-PT/invite?ref=DICA_DO_GEMINI" 

@app.route('/')
def home():
    try:
        # Puxa o preço real do Bitcoin para o teu site
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
            body {{ font-family: sans-serif; background: #0b0e11; color: white; text-align: center; padding: 20px; }}
            .card {{ background: #1e2329; border-radius: 15px; padding: 20px; border: 1px solid #ffb11a; display: inline-block; }}
            .btn {{ display: block; padding: 15px; margin-top: 20px; background: #ffb11a; color: black; text-decoration: none; font-weight: bold; border-radius: 10px; }}
        </style>
    </head>
    <body>
        <h1>🚀 IA SIGNAL BOT</h1>
        <div class="card">
            <p>BITCOIN AGORA</p>
            <h2 style="color: #ffb11a;">${preco_formatado}</h2>
            <p style="color: #0ecb81;">SINAL: COMPRA FORTE</p>
        </div>
        <br>
        <a href="https://www.binance.com  /referral/earn-together/refer2earn-usdc/claim?hl=pt&ref=GRO_28502_9GMCA&utm_source=default " class="btn">REIVINDICAR BÓNUS BINANCE</a>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)      
