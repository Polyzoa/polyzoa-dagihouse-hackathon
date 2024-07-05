import argparse
from scripts.generate_data import generate_dataframe
from scripts.train_model import train_and_select_model
from scripts.predict import predict_new_data, get_top_features
from pycaret.classification import load_model
import pandas as pd

def main(predict=False, read=False, compare=False, tune=False):
    """Runs the ML pipeline for prediction.

    - Generates data
    - Trains, interprets, selects a model
    - Predicts on new data & extracts top features (example provided)
    """
    if not predict:
        if not read:
            generate_dataframe()
            print("Data generation complete.")

        model = train_and_select_model(compare=compare, tune=tune)
        print("Model training, interpretation, and store complete.")

    with open('data/to_predict.json', 'r') as file:
        new_data = pd.read_json(file)

    predictions = predict_new_data(new_data)
    print("Prediction: ", predictions)

    model = load_model('models/best_model')
    top_features = get_top_features(model, new_data)
    print("Top features: ", top_features)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run ML pipeline for prediction.")
    parser.add_argument('-P', '--predict', action='store_true', help="Only run the prediction step.")
    parser.add_argument('-C', '--compare', action='store_true', help="Compare models and find the best one, taking longer to train.")
    parser.add_argument('-T', '--tune', action='store_true', help="Tune the model, taking longer to train.")
    parser.add_argument('-R', '--read', action='store_true', help="Use local csv 'token_data.csv' to train.")

    args = parser.parse_args()

    main(predict=args.predict, read=args.read, compare=args.compare, tune=args.tune)

"""
Usage instructions:

Note: Feature names and types should always allign between to_predict.py and token_data.py except the flag column which only exists in token_data.
      Meanwhile dummy data generator (scripts/generate_data.py) must allign in order to extract the expected features.

> python main.py
    It will generate dummy data and use them to train a lightGbm model, interpret and predict the record data/to_predict.json
> python main.py -R -C -T
    **Those can also be used separately**
    -R will do the above but will read local data from data/token_data.csv instead of generate,
    -C will run model comparison and select the best one instead of using lightGbm
    -T will run parameter tuning on the final model
    note: -C and -T will make it take long to run!!!
> python main.py -P
    It will load the existing model and predict the record data/to_predict.json
"""
