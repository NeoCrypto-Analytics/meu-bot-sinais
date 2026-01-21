from flask import Flask, jsonify
import requests

app = Flask(__name__)

def get_market_data():
    try:
        # Busca dados reais da Binance
        res = requests.get("https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT").json()
        price = float(res['lastPrice'])
        change = float(res['priceChangePercent'])
        
        if change > 0.1: sinal = "🚀 COMPRA"
        elif change < -0.1: sinal = "📉 VENDA"
        else: sinal = "⏳ AGUARDANDO"
        
        return {"price": f"{price:,.2f}", "sinal": sinal}
    except Exception:
        return {"price": "Indisponível", "sinal": "Erro de Conexão"}

@app.route('/')
def home():
    data = get_market_data()
    # Usamos chavetas duplas {{ }} no CSS para que o Python não as confunda com variáveis
    return f"""
    <!DOCTYPE html>
    <html lang="pt">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>IA Signal Bot - Ricardo</title>
        <style>
            body {{ background-color: #0d1117; color: white; font-family: sans-serif; text-align: center; padding: 50px; }}
            .card {{ background: #161b22; border: 1px solid #30363d; padding: 20px; border-radius: 15px; max-width: 400px; margin: 0 auto; }}
            .btn {{ display: block; background: #238636; color: white; padding: 15px; margin: 10px 0; border-radius: 8px; text-decoration: none; font-weight: bold; }}
            .sinal {{ font-size: 1.8em; color: #03ff00; margin: 15px 0; font-weight: bold; }}
            .price {{ font-size: 1.2em; color: #8b949e; }}
            .btn-plinko {{ background: #8a2be2; }}
            .status {{ color: #238636; font-size: 0.9em; margin-top: 10px; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h2>🤖 IA SIGNAL BOT</h2>
            <div class="price">BTC: $ {data['price']}</div>
            <div class="sinal">{data['sinal']}</div>
            
            <p class="status">● Conectado ao Mercado Global</p>
            
            <a href="https://www.bybit.com/invite?ref=9GMCA" class="btn">🔥 BINANCE/BYBIT: SINAIS VIP</a>
            <a href="#" class="btn btn-plinko">🎮 GAMING ZONE: BREVEMENTE</a>
            
            <p style="font-size: 0.7em; color: #8b949e; margin-top: 20px;">
                © Ricardo - Tecnologia & Trading 2026
            </p>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    # host='0.0.0.0' é importante para o bot funcionar online (Render/Replit)
    app.run(host='0.0.0.0', port=5000, debug=True)
    
