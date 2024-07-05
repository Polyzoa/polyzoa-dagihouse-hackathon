import pandas as pd
import argparse
from pycaret.anomaly import *

def load_data(filename):
    df = pd.read_csv(f"data/{filename}")
    return df

def preprocess_data(df):
    df.drop(columns=['flag'], inplace=True)
    return df

def run_anomaly_detection(df):
    exp_ano = setup(df)
    
    iforest = create_model('iforest')
    
    plot_model(iforest, save='results/')
    plot_model(iforest, plot='umap', save='results/')

def main(filename):
    df = load_data(filename)
    
    df = preprocess_data(df)
    
    run_anomaly_detection(df)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Anomaly detection using PyCaret.")
    parser.add_argument("-N", "--filename", type=str, help="Path to the CSV file containing data.")
    args = parser.parse_args()
    
    if args.filename:
        main(args.filename)
    else:
        print("Please provide a filename using -N or --filename argument.")
