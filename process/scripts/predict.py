import pandas as pd
import numpy as np
from pycaret.classification import load_model, predict_model
import shap

def predict_new_data(new_data):
    model = load_model('models/best_model')
    predictions = predict_model(model, data=new_data)
    return predictions

def get_top_features(model, data, top_n=4):
    """
    Extracts top features influencing predictions using SHAP explainer.

    - Handles PyCaret models and selects appropriate explainer (TreeExplainer or KernelExplainer)
    - Calculates SHAP feature importances (absolute mean)
    - Returns the top N features (default: 4) by their importance

    Args:
        model: Trained PyCaret model
        data: Pandas DataFrame with features
        top_n (int, optional): Number of top features to return. Defaults to 4.

    Returns:
        list: List of data column names representing the top features
    """
    if hasattr(model, 'steps'):
        for step_name, step in model.steps:
            if hasattr(step, 'predict'):
                base_model = step
                break
    else:
        base_model = model

    try:
        explainer = shap.TreeExplainer(base_model)
        shap_values = explainer.shap_values(data)
    except Exception as e:
        explainer = shap.KernelExplainer(base_model.predict, data)
        shap_values = explainer.shap_values(data)

    # For classification, shap_values might be a list (one for each class)
    if isinstance(shap_values, list):
        shap_values = shap_values[1]  # Take the SHAP values for the positive class

    shap_values = np.abs(shap_values).mean(axis=0)
    top_features = np.argsort(shap_values)[-top_n:]
    return data.columns[top_features]

if __name__ == "__main__":
    # Import json data to predict
    with open('data/to_predict.json', 'r') as file:
        new_data = pd.read_json(file)

    predictions = predict_new_data(new_data)
    print(predictions)

    model = load_model('models/best_model')
    top_features = get_top_features(model, new_data)
    print(top_features)
