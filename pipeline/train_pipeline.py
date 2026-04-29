import yaml
from src.data_ingestion import load_data
from src.preprocessing import preprocess_data, save_processed_data
from src.train import train_model, save_model
from src.logger import get_logger

logger = get_logger()

def load_config():
    with open("config/config.yaml", "r") as f:
        return yaml.safe_load(f)

def run_pipeline():

    config = load_config()

    df = load_data(config["data"]["raw_path"])
    df = preprocess_data(df)

    save_processed_data(df, config["data"]["processed_path"])

    model = train_model(
        df,
        config["train"]["test_size"],
        config["train"]["random_state"]
    )

    save_model(model, config["model"]["model_path"])

    logger.info("Training pipeline completed")

if __name__ == "__main__":
    run_pipeline()