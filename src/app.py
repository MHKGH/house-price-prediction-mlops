# src/app.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# 1. INITIALIZE APP
app = FastAPI()

# 2. LOAD THE ARTIFACT (The Brain)
# We load this once when the server starts
model = joblib.load("models/house_model.pkl")

# 3. DEFINE INPUT FORMAT (The Contract)
# We tell the API: "You must send us two numbers"
class HouseInput(BaseModel):
    size_sqft: int
    bedrooms: int

# 4. DEFINE THE ENDPOINT
@app.post("/predict")
def predict_price(data: HouseInput):
    # Extract data from the request
    # The model expects a list of inputs: [[size, rooms]]
    features = [[data.size_sqft, data.bedrooms]]
    
    # Ask the model for the answer
    predicted_price = model.predict(features)[0]
    
    return {
        "input_size": data.size_sqft,
        "input_bedrooms": data.bedrooms,
        "estimated_price": round(predicted_price, 2)
    }