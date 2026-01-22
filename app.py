from flask import Flask, jsonify
import requests

app = Flask(__name__)

def get_market_data():
    try:
        # Busca dados reais da Binance para o Bitcoin
        res = requests.get("https://api3.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT").json()
        price = float(res['lastPrice'])
        change = float(res['priceChangePercent'])
        
        if change > 0.1: sinal = "🚀 BUY SIGNAL"
        elif change < -0.1: sinal = "📉 SELL SIGNAL"
        else: sinal = "⏳ NEUTRAL / WAIT"
        
        return {"price": f"{price:,.2f}", "sinal": sinal}
    except Exception:
        return {"price": "Offline", "sinal": "Connection Error"}

@app.route('/')
def home():
    data = get_market_data()
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AI Signal & Gaming Bot</title>
        <style>
            body {{ background-color: #0d1117; color: white; font-family: sans-serif; text-align: center; padding: 20px; }}
            .card {{ background: #161b22; border: 1px solid #30363d; padding: 25px; border-radius: 20px; max-width: 450px; margin: 0 auto; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }}
            h2 {{ color: #58a6ff; margin-bottom: 5px; }}
            .price {{ font-size: 1.4em; color: #8b949e; margin-bottom: 10px; }}
            .sinal {{ font-size: 2em; color: #3fb950; font-weight: bold; margin: 20px 0; text-shadow: 0 0 10px rgba(63, 185, 80, 0.5); }}
            .btn {{ display: block; padding: 15px; margin: 12px 0; border-radius: 10px; text-decoration: none; font-weight: bold; transition: 0.3s; }}
            .btn-crypto {{ background: #238636; color: white; }}
            .btn-crypto:hover {{ background: #2ea043; }}
            .btn-gaming {{ background: #8a2be2; color: white; }}
            .btn-gaming:hover {{ background: #9d4edd; }}
            .status {{ color: #3fb950; font-size: 0.85em; margin-top: 15px; }}
            .chart-container {{ margin-top: 20px; border-radius: 10px; overflow: hidden; border: 1px solid #30363d; }}
            .footer {{ font-size: 0.7em; color: #8b949e; margin-top: 25px; line-height: 1.5; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h2>🤖 AI SIGNAL BOT</h2>
            <div class="price">BTC/USDT: ${data['price']}</div>
            <div class="sinal">{data['sinal']}</div>
            <p class="status">● Global Market Data Connected</p>
            
            <a href="https://www.bybit.com/invite?ref=9GMCA" class="btn btn-crypto">🔥 GET CRYPTO SIGNALS (VIP)</a>
            
            <a href="https://bc.fun/i-4a86j0t7s-n/" class="btn btn-gaming">🎰 INTERNATIONAL GAMING ZONE</a>

            <div class="chart-container">
                <iframe src="https://s.tradingview.com/widgetembed/?symbol=BINANCE%3ABTCUSDT&interval=60&theme=dark&style=1&timezone=Etc%2FUTC&locale=en" 
                        width="100%" height="250" frameborder="0" allowtransparency="true" scrolling="no"></iframe>
            </div>
            <div class="footer">
                © 2026 NeoCrypto Analytics - Global Edition<br>
                High Risk Trading & Gaming. Play Responsibly.
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
