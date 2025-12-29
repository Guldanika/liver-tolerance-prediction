import bentoml
from bentoml.io import JSON
import joblib
import numpy as np
import pandas as pd

model = joblib.load("best_lightgbm_model.pkl")
scaler = joblib.load("scaler.pkl")
selected_genes = joblib.load("selected_top_500_genes.pkl")

service = bentoml.Service("ToleranceService")

@service.api(input=JSON(), output=JSON())
def predict(input_data: dict) -> dict:
    values = np.array(input_data["expression_values"])
    if len(values) != 500:
        return {"error": "Expected exactly 500 expression values"}
    
    df = pd.DataFrame([values], columns=selected_genes)
    scaled = scaler.transform(df)
    proba = model.predict_proba(scaled)[0, 1]
    
    return {
        "probability_of_tolerance": float(proba),
        "predicted_class": int(proba >= 0.5)
    }
