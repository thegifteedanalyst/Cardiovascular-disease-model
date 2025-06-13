# 🫀 Cardiovascular Disease Predictor

A simple and interactive web app built with **Streamlit** that uses a trained machine learning model to predict the risk of cardiovascular disease based on user inputs like age, cholesterol, and blood pressure.

🔗 **Live App:** [Click here to try it out!](https://your-name-your-app.streamlit.app)  
📦 **Model File:** Trained with scikit-learn (RandomForestClassifier)

---

## 🚀 Features

- Predicts cardiovascular disease risk instantly
- Collects inputs such as age, chest pain type, cholesterol level, etc.
- Simple, user-friendly interface
- Built with Python, Streamlit, and scikit-learn

---

## 📊 Input Features

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol Level
- Fasting Blood Sugar
- Resting ECG
- Maximum Heart Rate
- Exercise-Induced Angina
- Oldpeak (ST depression)
- ST Slope

---

## 🧠 How It Works

This app uses a pre-trained model (`cardiovascular_disease_model.pkl`) to predict whether a person has a high risk of cardiovascular disease (`Yes` or `No`) based on medical input data.

---

## 🛠 Tech Stack

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [scikit-learn](https://scikit-learn.org/)

---

## ▶️ Run Locally

```bash
git clone https://github.com/yourusername/cardiovascular-predictor.git
cd cardiovascular-predictor
pip install -r requirements.txt
streamlit run cardv.py
