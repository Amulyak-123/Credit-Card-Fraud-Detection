from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

# ✅ Load Trained Model
model = joblib.load("models/fraud_detection.pkl")

# ✅ Define API
app = FastAPI()

# ✅ Define Input Model (Must Match `train_model.py` Features)
class Transaction(BaseModel):
    Amount_Scaled: float
    Transaction_Hour: int
    Transaction_Day: int
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float

@app.get("/")
def home():
    return {"message": "Welcome to the Fraud Detection API! Use /predict to check transactions."}

@app.get("/favicon.ico")
async def favicon():
    return {}

# ✅ Prediction Endpoint
@app.post("/predict")
async def predict(transaction: Transaction):
    try:
        # ✅ Convert Input to DataFrame
        transaction_data = pd.DataFrame([transaction.dict()])

        # ✅ Ensure input matches model features
        transaction_data = transaction_data.reindex(columns=model.feature_names_in_, fill_value=0)

        # ✅ Make Prediction
        prediction = model.predict(transaction_data)[0]
        return {"fraud": bool(prediction)}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction error: {str(e)}")
