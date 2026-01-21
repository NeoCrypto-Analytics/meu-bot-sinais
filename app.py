from flask import flask
import requests

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
            <a href="https://www.bybit.com/invite?ref=9GNCA" class="btn">💰 BINANCE/BYBIT: SINAIS VIP</a>
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
    # Removido o erro de sintaxe que estava no final desta linha
    app.run(host='0.0.0.0', port=5000)
