import joblib
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify

# === Load artifacts ===
model = joblib.load("model/best_lightgbm_model.pkl")
scaler = joblib.load("model/scaler.pkl")
selected_genes = joblib.load("model/selected_top_500_genes.pkl")

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Проверка входа
    missing = [g for g in selected_genes if g not in data]
    if missing:
        return jsonify({
            "error": "Missing genes",
            "missing_genes": missing[:10]  # не спамить 500
        }), 400

    # 1. JSON → DataFrame (1 x 500)
    X = pd.DataFrame([[data[g] for g in selected_genes]],
                     columns=selected_genes)

    # 2. Scaling
    X_scaled = scaler.transform(X)

    # 3. Prediction
    proba = model.predict_proba(X_scaled)[0, 1]
    prediction = int(proba >= 0.5)

    return jsonify({
        "prediction": prediction,
        "probability_tolerance": round(float(proba), 4),
        "model": "LightGBM (tuned)",
        "note": "Research-grade decision support only"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
