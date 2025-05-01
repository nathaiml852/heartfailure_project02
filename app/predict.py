# app/predict.py

import pandas as pd
import xgboost as xgb
import prometheus_client
from prometheus_client import Counter, Histogram
from app.model_loader import load_model
import time

model = load_model()

# Define Prometheus metrics
PREDICTION_COUNT = Counter("predictions_total", "Total prediction requests", ["status"])
PREDICTION_LATENCY = Histogram("prediction_duration_seconds", "Time spent in prediction")

@PREDICTION_LATENCY.time()
def predict_death_event(age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction,
                        high_blood_pressure, platelets, serum_creatinine, serum_sodium,
                        sex, smoking, time):
    try:
        input_dict = {
            "age": age,
            "anaemia": anaemia,
            "creatinine_phosphokinase": creatinine_phosphokinase,
            "diabetes": diabetes,
            "ejection_fraction": ejection_fraction,
            "high_blood_pressure": high_blood_pressure,
            "platelets": platelets,
            "serum_creatinine": serum_creatinine,
            "serum_sodium": serum_sodium,
            "sex": sex,
            "smoking": smoking,
            "time": time
        }
        df = pd.DataFrame([input_dict])
        dmatrix = xgb.DMatrix(df)
        prediction = int(model.predict(dmatrix)[0] >= 0.5)

        PREDICTION_COUNT.labels(status="success").inc()

        return "YES - Death event likely." if prediction == 1 else "NO - Death event not likely."
    except Exception as e:
        PREDICTION_COUNT.labels(status="error").inc()
        return f"Prediction error: {str(e)}"