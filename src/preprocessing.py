from sklearn.preprocessing import LabelEncoder
from src.logger import get_logger

logger = get_logger()

def preprocess_data(df):

    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

    df.drop(columns=['Cabin', 'Ticket', 'Name', 'PassengerId'], inplace=True, errors='ignore')

    le = LabelEncoder()
    for col in df.select_dtypes(include='object').columns:
        df[col] = le.fit_transform(df[col])

    logger.info("Data preprocessing completed")

    return df


def save_processed_data(df, path):
    df.to_csv(path, index=False)
    logger.info(f"Processed data saved at {path}")