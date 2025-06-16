import pickle
import pandas as pd

def load_model():
    with open("model/house_price_model_linear_regression.pkl", "rb") as f:
        return pickle.load(f)

def preprocess_input(bedrooms, bathrooms, area, lot_area, floors, waterfront, views,
                     condition, grade, schools, distance, age):
    
    df = pd.DataFrame([{
        "number of bedrooms": bedrooms,
        "number of bathrooms": bathrooms,
        "living area": area,
        "lot area": lot_area,
        "number of floors": floors,
        "waterfront present": waterfront,
        "number of views": views,
        "condition of the house": condition,
        "grade of the house": grade,
        "Number of schools nearby": schools,
        "Distance from the airport": distance,
        "House Age": age,
        "price_per_sqft": 0,
        "lot_utilization_ratio": area / lot_area if lot_area != 0 else 0,
        "bath_per_bed": bathrooms / bedrooms if bedrooms != 0 else 0,
        "schools_per_km": schools / distance if distance != 0 else 0
    }])
    
    return df
