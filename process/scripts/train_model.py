from pycaret.classification import *
from .preprocess_data import load_and_preprocess_data
import matplotlib.pyplot as plt
import os
import warnings

def train_and_select_model(compare: bool, tune: bool):
    """
    Trains, interprets (commented out due to known issue), and selects
    the best classification model using PyCaret. Saves the best model.

    - Loads and preprocesses data
    - Compares models and selects the best one (LightGBM used here)
    - Finalizes the selected model
    - Saves the best model ('models/best_model')
    """
    X_train, X_test, y_train, y_test = load_and_preprocess_data()

    # Combine X_train and y_train for PyCaret
    train_data = X_train.copy()
    train_data['flag'] = y_train

    s = setup(data=train_data, target='flag')

    if compare:
        model = compare_models()
    else:
        model = create_model('lightgbm') # Use lightgbm as default

    if tune:
        model = tune_model(model, optimize = 'AUC') # Can also use F1 but AUC is good for balance

    final_model = finalize_model(model)

    # Interpret model
    os.makedirs('results', exist_ok=True)
    interpret_model(model, plot='summary', save='results/')
    interpret_model(model, plot='correlation', save='results/')
    # interpret_model(model, plot='reason', save='results/')
    # interpret_model(model, plot='msa', save='results/')

    os.makedirs('models', exist_ok=True)
    save_model(final_model, 'models/best_model')

    return final_model

if __name__ == "__main__":
    model = train_and_select_model()
    print("Model training, interpretation, and selection complete.")
