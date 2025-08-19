import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np


def train_model():
    # Sample Data
    data = {
        'vehicle_type': ['2wheeler', '2wheeler', '4wheeler', '4wheeler'],
        'distance': [50, 100, 50, 100],
        'fuel_efficiency': [40, 40, 15, 15],  # km per litre
        'petrol_price': [100, 100, 100, 100],  # Price per litre
        'accommodation_type': ['PG', 'HomeStay', 'Resort', 'PG'],
        'food_cost': [200, 300, 500, 400],  # Daily food cost
        'travel_cost': [150, 300, 200, 400]  # Total travel cost
    }

    df = pd.DataFrame(data)
    # Convert categorical to numeric for ML
    df['vehicle_type'] = df['vehicle_type'].map({'2wheeler': 1, '4wheeler': 2})
    df['accommodation_type'] = df['accommodation_type'].map({'PG': 1, 'HomeStay': 2, 'Resort': 3})

    X = df[['vehicle_type', 'distance', 'fuel_efficiency', 'petrol_price', 'accommodation_type', 'food_cost']]
    y = df['travel_cost']

    model = LinearRegression()
    model.fit(X, y)

    return model


def predict_cost(model, vehicle_type, distance, fuel_efficiency, petrol_price, accommodation_type, food_cost):
    input_data = np.array([[vehicle_type, distance, fuel_efficiency, petrol_price, accommodation_type, food_cost]])
    predicted_cost = model.predict(input_data)
    return predicted_cost[0]
