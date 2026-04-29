from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
from src.logger import get_logger

logger = get_logger()

def train_model(df, test_size, random_state):

    X = df.drop('Survived', axis=1)
    y = df['Survived']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    logger.info("Model training completed")

    return model


def save_model(model, path):
    joblib.dump(model, path)
    logger.info(f"Model saved at {path}")