import joblib
import xgboost as xgb

def load_model():
    model=xgb.Booster()
    model.load_model("models/xgboost-model.json") 
    return  model