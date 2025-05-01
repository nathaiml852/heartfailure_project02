import pandas as pd
import xgboost as xgb
from app.model_loader import load_model
from app.metrics import (
    PREDICTION_COUNT,
    PREDICTION_LATENCY,
    PREDICTION_ERROR_TYPE,
    INPUT_ANOMALY_COUNT,
    REQUEST_SOURCE_COUNT
)

# Load model
model = load_model()

# Define the prediction function with Prometheus metrics tracking
@PREDICTION_LATENCY.time()
def predict_death_event(age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction,
                        high_blood_pressure, platelets, serum_creatinine, serum_sodium,
                        sex, smoking, time, source="gradio"):
    try:
        # Track the source of the request (optional)
        REQUEST_SOURCE_COUNT.labels(source=source).inc()

        # Basic input anomaly detection (example: negative platelets)
        if platelets <= 0:
            INPUT_ANOMALY_COUNT.labels(field="platelets").inc()

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

        # Make the prediction
        prediction = int(model.predict(dmatrix)[0] >= 0.5)

        # Count successful prediction
        PREDICTION_COUNT.labels(status="success").inc()

        return "YES - Death event likely." if prediction == 1 else "NO - Death event not likely."

    except ValueError as ve:
        PREDICTION_COUNT.labels(status="error").inc()
        PREDICTION_ERROR_TYPE.labels(error_type="value_error").inc()
        return f"Input value error: {str(ve)}"

    except KeyError as ke:
        PREDICTION_COUNT.labels(status="error").inc()
        PREDICTION_ERROR_TYPE.labels(error_type="key_error").inc()
        return f"Missing input field: {str(ke)}"

    except Exception as e:
        PREDICTION_COUNT.labels(status="error").inc()
        PREDICTION_ERROR_TYPE.labels(error_type="unknown").inc()
        return f"Unexpected error: {str(e)}"
