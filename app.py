from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="pt">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>IA Signal Bot - Ricardo</title>
        <style>
            body { background-color: #0d1117; color: white; font-family: sans-serif; text-align: center; padding: 50px; }
            .card { background: #161b22; border: 1px solid #30363d; padding: 20px; border-radius: 15px; max-width: 400px; margin: 0 auto; }
            .btn { display: block; background: #238636; color: white; padding: 15px; margin: 10px 0; border-radius: 8px; text-decoration: none; font-weight: bold; }
            .btn-plinko { background: #8a2be2; }
            .status { color: #238636; font-size: 0.9em; margin-top: 10px; }
        </style>
    </head>
    <body>
        <div class="card">
            <h2>🤖 IA SIGNAL BOT</h2>
            <p>Conectado ao Mercado Global</p>
            
            <a href="https://www.bybit.com/invite?ref=9GMCA" class="btn">💰 BINANCE/BYBIT: SINAIS VIP</a>
            
            <a href="#" class="btn btn-plinko">🎮 GAMING ZONE: BREVEMENTE</a>
            
            <div class="status">● Sistema Ativo (UptimeRobot Protected)</div>
            <hr style="border: 0.5px solid #30363d; margin: 20px 0;">
            <p style="font-size: 0.7em; color: #8b949e;">Ricardo - Tecnologia & Trading © 2026<br>
            Aviso: O trading envolve riscos. Jogue com responsabilidade.</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)from flask import Flask
import requests

app = Flask(__name__)

# --- CONFIGURAÇÃO DE LUCRO ---
LINK_BINANCE = "https://www.binance.com/referral/earn-together/refer2earn-usdc/claim?hl=pt&ref=GRO_28502_9GMCA&utm_source=default"
LINK_BYBIT = "https://www.bybit.eu/invite?ref=78KZLEQ"

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
            body {{ font-family: sans-serif; background: #0b0e11; color: white; text-align: center; padding: 20px; }}
           .card {{ background: #1e2329; border-radius: 20px; padding: 30px; border: 1px solid #ffb11a; display: inline-block; margin-top: 20px; }}
           .price {{ font-size: 3em; color: #ffb11a; font-weight: bold; }}
           .btn {{ display: block; padding: 18px; margin: 15px 0; border-radius: 12px; text-decoration: none; font-weight: bold; font-size: 1.2em; transition: 0.3s; }}
           .binance {{ background: #f3ba2f; color: black; }}
           .bybit {{ background: #000000; color: white; border: 2px solid #ffb11a; }}
        </style>
    </head>
    <body>
        <h1>🤖 IA SIGNAL BOT <span style="color:#ffb11a;">PRO</span></h1>
        <div class="card">
            <p>BITCOIN (BTC/USDT)</p>
            <div class="price">${preco_formatado}</div>
            <p style="color: #0ecb81; font-weight: bold;">⚡ SINAL: COMPRA DETETADA</p>
        </div>
        
        <h3>Regista-te para copiar o sinal:</h3>
        <a href="{LINK_BINANCE}" class="btn binance">REIVINDICAR BÓNUS BINANCE</a>
        <a href="{LINK_BYBIT}" class="btn bybit">REIVINDICAR BÓNUS BYBIT</a>
        
        <p style="font-size: 0.7em; color: gray; margin-top: 50px;">Análise 24h via IA ligada às APIs oficiais.</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
