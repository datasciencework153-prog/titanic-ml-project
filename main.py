from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load model & scaler
model = joblib.load("titanic_model.pkl")
scaler = joblib.load("scaler.pkl")


# HOME PAGE
@app.route("/")
def home():
    return render_template("index.html")


# PREDICT FORM
@app.route("/predict_form", methods=["POST"])
def predict_form():
    form = request.form
    data = {key: float(form[key]) if form[key] != "" else 0 for key in form}

    df = pd.DataFrame([data])

    try:
        df = df.reindex(columns=scaler.feature_names_in_, fill_value=0)
        scaled = scaler.transform(df)
    except:
        scaled = df

    pred = model.predict(scaled)[0]
    prob = model.predict_proba(scaled)[0][1]

    status = "SURVIVE ✅" if pred else "NOT SURVIVE ❌"

    # ✅ ONLY ONE RETURN
    return render_template(
        "index.html",
        result=status,
        probability=round(prob * 100, 2)
    )


# TEST ROUTE
@app.route("/test")
def test():
    return "Working fine 👍"


# RUN APP
if __name__ == "__main__":
    app.run(debug=True)