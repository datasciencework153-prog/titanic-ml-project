from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("models/titanic_model.pkl")

@app.route("/")
def home():
    return "Titanic ML API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return jsonify({"prediction": int(prediction[0])})
