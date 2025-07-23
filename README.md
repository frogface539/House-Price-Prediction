# 🏡 House Price Prediction Web App

An interactive machine learning web application that predicts house prices in India using engineered real estate data and advanced regression models. Built with **Streamlit** for ease of use and real-time inference.

---

## 🔍 Key Features

* 📐 **Predicts house prices** based on over **16 input features**
* 🛠️ **Feature Engineering** includes:

  * `price_per_sqft`
  * `bath_per_bed`
  * `lot_utilization_ratio`
  * `schools_per_km`
  * `house_age`
* 🤖 Implements 3 Regression Models:

  * **Linear Regression**
  * **Support Vector Regression (SVR)**
  * **Random Forest Regressor** (🚀 **best performer with 99% R²**)
* 💾 Model saved using `pickle`
* ⚖️ Preprocessing includes **StandardScaler** for feature scaling
* 🖥️ Deployed via **Streamlit** for live predictions

---
## 💻 Demo

🔗 https://indian-house-price-prediction.streamlit.app/

---

## 🧱 Project Structure

```
House-Price-Predictor/
├── app.py                  # Main Streamlit web app
├── utils.py                # Feature engineering & preprocessing logic
├── model/
│   ├── house_price_model.pkl  # Trained Random Forest model
│   └── scaler.pkl             # StandardScaler used in training
├── dataset/
│   └── House Price India.csv  # Training data (not pushed to GitHub)
└── requirements.txt        # Python dependencies
```

---

## 🚀 How to Run Locally

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/House-Price-Predictor.git
   cd House-Price-Predictor
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**:

   ```bash
   streamlit run app.py
   ```

---

## 📊 Model Performance

| Model             | R² Score (Accuracy) |
| ----------------- | ------------------- |
| Linear Regression | \~91%               |
| SVR               | \~64%               |
| Random Forest     | ⭐ **99% (Best)**    |

---

## 📦 Libraries Used

* `pandas` — Data manipulation
* `numpy` — Numerical operations
* `scikit-learn` — ML algorithms, scaling, model persistence
* `streamlit` — UI framework for web deployment
* `matplotlib`, `seaborn` — For EDA (Exploratory Data Analysis)

---
## 👤 Author

**Lakshay Jain**
🔗 [LinkedIn](https://www.linkedin.com/in/lakshay-jain-a48979289/)
🐙 [GitHub](https://github.com/frogface539)

> Contributions and suggestions are welcome! Feel free to fork the project and enhance it further.
