import yaml
from src.predict import load_model, predict

def load_config():
    with open("config/config.yaml", "r") as f:
        return yaml.safe_load(f)

def run_inference():

    config = load_config()

    model = load_model(config["model"]["model_path"])

    sample_data = {
        'Pclass': 3,
        'Sex': 1,
        'Age': 22,
        'SibSp': 1,
        'Parch': 0,
        'Fare': 7.25,
        'Embarked': 2
    }

    result = predict(model, sample_data)

    print("Prediction:", result)

if __name__ == "__main__":
    run_inference()