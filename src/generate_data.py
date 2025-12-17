# src/generate_data.py
import pandas as pd
import random

# 1. Define the data
data = {
    "size_sqft": [],
    "bedrooms": [],
    "price": []
}

# 2. Generate 100 fake houses
for _ in range(100):
    size = random.randint(500, 3500)
    rooms = random.randint(1, 5)
    
    # Logic: Price is Size * 100 + Rooms * 10,000
    price = (size * 100) + (rooms * 10000)
    
    data["size_sqft"].append(size)
    data["bedrooms"].append(rooms)
    data["price"].append(price)

# 3. Convert dictionary to DataFrame
# (Fill in the blank below!)
df = pd.DataFrame(data) 

# 4. Save to CSV inside the 'data' folder
# (Fill in the blank: use index=False)
df.to_csv("/home/hemanth/Documents/MLOps/house-price-api/data/house_prices.csv", index=False)

print("Data generated successfully in data/house_prices.csv")