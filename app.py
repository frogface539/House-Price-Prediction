import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load the trained model
with open("model/house_price_model_linear_regression.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="House Price Predictor", layout="centered")
st.title("🏡 House Price Prediction (India)")
st.markdown("Enter house details below to estimate the market price.")

# === User Inputs ===
bedrooms = st.number_input("Number of Bedrooms", 1, 10, 3)
bathrooms = st.number_input("Number of Bathrooms", 1.0, 10.0, 2.0)
living_area = st.number_input("Living Area (in sq ft)", 500, 10000, 2000)
lot_area = st.number_input("Lot Area (in sq ft)", 1000, 20000, 4000)
floors = st.number_input("Number of Floors", 1.0, 3.0, 1.0)
waterfront = st.selectbox("Waterfront Present?", [0, 1])
views = st.slider("Number of Views", 0, 4, 1)
condition = st.slider("Condition of the House", 1, 5, 3)
grade = st.slider("Grade of the House", 1, 13, 7)
schools_nearby = st.slider("Number of Schools Nearby", 0, 10, 3)
distance_airport = st.slider("Distance from Airport (km)", 1, 50, 10)
house_age = st.slider("Age of the House (years)", 0, 120, 10)

# === Feature Engineering ===
lot_utilization_ratio = living_area / lot_area if lot_area != 0 else 0
bath_per_bed = bathrooms / bedrooms if bedrooms != 0 else 0
schools_per_km = schools_nearby / (distance_airport + 1)

input_data = pd.DataFrame([{
    'number of bedrooms': bedrooms,
    'number of bathrooms': bathrooms,
    'living area': living_area,
    'lot area': lot_area,
    'number of floors': floors,
    'waterfront present': waterfront,
    'number of views': views,
    'condition of the house': condition,
    'grade of the house': grade,
    'Number of schools nearby': schools_nearby,
    'Distance from the airport': distance_airport,
    'House Age': house_age,
    'price_per_sqft': 0,
    'lot_utilization_ratio': lot_utilization_ratio,
    'bath_per_bed': bath_per_bed,
    'schools_per_km': schools_per_km
}])

# === Predict ===
if st.button(" Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f" **Predicted House Price:** ₹{prediction:,.2f}")
