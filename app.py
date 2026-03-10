from flask import Flask, render_template, jsonify
import yfinance as yf
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model

app = Flask(__name__)

print("🔥 Loading 92% RELIANCE model...")
model = load_model('models/week3_bidirectional.h5', compile=False)
model.compile(optimizer='adam', loss='mse')
print("✅ Model LOADED!")


# -----------------------------
# DASHBOARD
# -----------------------------
@app.route('/')
def dashboard():
    return render_template('dashboard.html')


# -----------------------------
# PREDICTION API
# -----------------------------
@app.route('/api/predict')
def predict():
    try:
        print("📡 Fetching RELIANCE data...")
        df = yf.download("RELIANCE.NS", period="2y", progress=False)

        # Force 1D Series
        close_prices = df['Close'].squeeze()
        volume_data = df['Volume'].squeeze()

        # -------- INDICATORS --------
        delta = close_prices.diff()
        gain = delta.where(delta > 0, 0).rolling(14).mean()
        loss = -delta.where(delta < 0, 0).rolling(14).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))

        ema12 = close_prices.ewm(span=12).mean()
        ema26 = close_prices.ewm(span=26).mean()
        macd = ema12 - ema26

        volume_ma = volume_data.rolling(20).mean()
        returns = close_prices.pct_change()
        clean_close = close_prices.ewm(span=5).mean()

        data = pd.DataFrame({
            'Clean_Close': clean_close,
            'Volume': volume_data,
            'RSI': rsi,
            'MACD': macd,
            'Volume_MA': volume_ma,
            'Returns': returns
        }).dropna()

        # -------- SCALING --------
        data_min = data.min()
        data_max = data.max()
        data_scaled = (data - data_min) / (data_max - data_min)

        X = data_scaled.values[-60:].reshape(1, 60, 6)

        # -------- PREDICTION --------
        pred_scaled = model.predict(X, verbose=0)[0][0]

        current_price = data['Clean_Close'].iloc[-1]
        price_min = data_min['Clean_Close']
        price_max = data_max['Clean_Close']

        pred_price = pred_scaled * (price_max - price_min) + price_min
        change_pct = ((pred_price - current_price) / current_price) * 100

        # -------- SIGNAL (NO EMOJIS) --------
        if change_pct > 1:
            signal = "BUY"
        elif change_pct < -1:
            signal = "SELL"
        else:
            signal = "HOLD"

        print(
            f"📊 Current ₹{current_price:.2f} → "
            f"Tomorrow ₹{pred_price:.2f} "
            f"({change_pct:+.2f}%) [{signal}]"
        )

        return jsonify({
            "stock": "RELIANCE",
            "current": f"₹{current_price:.2f}",
            "tomorrow": f"₹{pred_price:.2f}",
            "change": f"{change_pct:.2f}",   # ← NO %
            "signal": signal
        })

    except Exception as e:
        print("❌ ERROR:", e)
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


# -----------------------------
# RUN APP
# -----------------------------
if __name__ == "__main__":
    print("🌟 Starting RELIANCE AI Predictor...")
    app.run(host="0.0.0.0", port=5000, debug=True)