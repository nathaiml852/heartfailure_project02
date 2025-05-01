import pandas as pd
import xgboost as xgb
from app.model_loader import load_model
from app.metrics import PREDICTION_COUNT, PREDICTION_LATENCY,PREDICTION_ERROR_TYPE

# Load model
model = load_model()

# Define the prediction function with Prometheus metrics tracking
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
        
        # Prepare the input for the model
        df = pd.DataFrame([input_dict])
        dmatrix = xgb.DMatrix(df)
        
        # Make the prediction
        prediction = int(model.predict(dmatrix)[0] >= 0.5)

        # Increment prediction success count
        PREDICTION_COUNT.labels(status="success").inc()

        return "YES - Death event likely." if prediction == 1 else "NO - Death event not likely."

    except Exception as e:
        # Increment prediction error count
        PREDICTION_COUNT.labels(status="error").inc()
        return f"Prediction error: {str(e)}"
