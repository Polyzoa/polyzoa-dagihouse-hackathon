import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_preprocess_data(file_path='data/token_data.csv'):
    """
    Loads and preprocesses data from 'data/token_data.csv'.

    - Reads CSV data
    - Splits data into features (X) and target variable (y)
    - Splits data into training and testing sets (80%/20% split, stratified)

    Returns:
        X_train, X_test, y_train, y_test: Split data for training and testing.
    """
    df = pd.read_csv(file_path)

    X = df.drop(columns=['flag'])
    y = df['flag']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = load_and_preprocess_data()
    print("Data preprocessing complete.")
