# 🏡 House Price Prediction Web App

A complete machine learning project that predicts house prices in India using engineered real estate data and regression models.

## 🔧 Features

- 🔍 Predict house prices based on 16+ features
- ⚙️ Feature Engineering: 
  - `price_per_sqft`
  - `bath_per_bed`
  - `lot_utilization_ratio`
  - `schools_per_km`
  - `House Age`
- 📊 Uses 3 regression techniques:
  - **Linear Regression**
  - **Support Vector Regression (SVR)**
  - **Random Forest Regressor (best model with 99% R²)**
- ✅ Fully deployed using **Streamlit**
- 💾 Model persistence using `pickle`
- 📈 Feature scaling with `StandardScaler`

## 📁 Project Structure
```
├── app.py # Streamlit app
├── model/
│ ├── house_price_model.pkl
│ └── scaler.pkl
├── utils.py # Feature engineering & preprocessing
├── dataset/
│ └── House Price India.csv
└── requirements.txt
```

## 🚀 How to Run

1. Clone the repo  
2. Install requirements:
pip install -r requirements.txt

3. Launch the app:
streamlit run app.py


## 📊 Results

| Model             | Accuracy (R² Score) |
|------------------|---------------------|
| Linear Regression| ~91%                |
| SVR              | ~64%                |
| Random Forest    | **99%**             |

## 📌 Libraries Used

- pandas
- numpy
- scikit-learn
- Streamlit
- matplotlib, seaborn (EDA)

