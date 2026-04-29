# tests/test_data.py

import pandas as pd
from src.preprocessing import preprocess_data

def test_preprocessing():

    sample = pd.DataFrame({
        'Age': [None, 25],
        'Embarked': [None, 'S'],
        'Cabin': ['C85', None],
        'Ticket': ['12345', '67890'],
        'Name': ['A', 'B'],
        'PassengerId': [1, 2],
        'Sex': ['male', 'female']
    })

    processed = preprocess_data(sample)

    assert processed.isnull().sum().sum() == 0
    print("✅ Data preprocessing test passed")