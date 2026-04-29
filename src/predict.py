import joblib
import pandas as pd

def load_model(path):
    return joblib.load(path)

def predict(model, sample):
    df = pd.DataFrame([sample])
    return model.predict(df)