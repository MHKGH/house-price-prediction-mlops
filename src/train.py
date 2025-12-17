# src/train.py
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# 1. LOAD DATA
# We read the file you just created
print("Loading data...")
df = pd.read_csv("/home/hemanth/Documents/MLOps/house-price-api/data/house_prices.csv")

# 2. SEPARATE INPUTS (X) AND OUTPUT (y)
# Inputs: Size and Bedrooms
X = df[["size_sqft", "bedrooms"]]
# Output: Price
y = df["price"]

# 3. TRAIN THE MODEL
# This is where the "learning" happens
print("Training model...")
model = LinearRegression()
model.fit(X, y)

# 4. SAVE THE ARTIFACT
# We save the trained model to a file so we can use it later
print("Saving model to models/house_model.pkl...")
joblib.dump(model, "/home/hemanth/Documents/MLOps/house-price-api/models/house_model.pkl")

print("Training Complete!")