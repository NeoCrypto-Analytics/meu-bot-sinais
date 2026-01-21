from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Função para buscar dados reais da Binance
def get_market_data():
    try:
        res = requests.get("https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT").json()
        price = float(res['lastPrice'])
        change = float(res['priceChangePercent'])
        
        if change > 0.1: sinal = "🚀 COMPRA"
        elif change < -0.1: sinal = "📉 VENDA"
        else: sinal = "⏳ AGUARDANDO"
        
        return {"price": f"${price:,.2f}", "sinal": sinal}
    except:
        return {"price": "Indisponível", "sinal": "Erro de Conexão"}

@app.route('/api/status')
def status():
    return jsonify(get_market_data())

@app.route('/')
def home():
    data = get_market_data()
    return f"""
    <!DOCTYPE html>
    <html lang="pt">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>IA Signal Bot - Ricardo</title>
        <style>
            body {{ background-color: #0d1117; color: white; font-family: sans-serif; text-align: center; padding: 20px; }}
            .card {{ background: #161b22; border: 1px solid #30363d; padding: 20px; border-radius: 15px; max-width: 400px; margin: 0 auto; }}
            .btn {{ display: block; background: #238636; color: white; padding: 15px; margin: 10px 0; border-radius: 8px; text-decoration: none; font-weight: bold; }}
            .sinal {{ font-size: 1.8em; color: #00ff00; margin: 15px 0; font-weight: bold; }}
            .price {{ font-size: 1.2em; color: #8b949e; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h2>🤖 IA SIGNAL BOT</h2>
            <div id="price" class="price">BTC: {data['price']}</div>
            <div id="sinal" class="sinal">{data['sinal']}</div>
            <a href="https://www.bybit.com/invite?ref=9GNCA" class="btn">💰 OPERAR AGORA (BYBIT)</a>
            <p style="font-size: 0.7em; color: #8b949e;">Sistema Ativo & Atualizado</p>
        </div>

        <script>
            setInterval(async () => {{
                try {{
                    const res = await fetch('/api/status');
                    const json = await res.json();
                    document.getElementById('price').innerText = 'BTC: ' + json.price;
                    document.getElementById('sinal').innerText = json.sinal;
                }} catch (e) {{ console.log("Erro ao atualizar"); }}
            }}, 5000);
        </script>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
