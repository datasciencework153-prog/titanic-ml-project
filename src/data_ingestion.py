import pandas as pd
from src.logger import get_logger

logger = get_logger()

def load_data(path):
    df = pd.read_csv(path)
    logger.info("Data loaded successfully")
    return df