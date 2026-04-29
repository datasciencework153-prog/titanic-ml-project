# tests/test_model.py

import pandas as pd
from src.train import train_model

def test_model_training():

    df = pd.DataFrame({
        'Pclass': [1, 3],
        'Sex': [0, 1],
        'Age': [22, 25],
        'SibSp': [1, 0],
        'Parch': [0, 0],
        'Fare': [7.25, 71.83],
        'Embarked': [2, 0],
        'Survived': [0, 1]
    })

    model = train_model(df, 0.2, 42)

    assert model is not None
    print("✅ Model training test passed")