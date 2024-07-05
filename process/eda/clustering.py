import pandas as pd
import argparse
from pycaret.clustering import *

def load_data(filename):
    df = pd.read_csv(f"data/{filename}")
    return df

def preprocess_data(df):
    df = df[df['flag'] == True]
    df.drop(columns=['flag'], inplace=True)
    return df

def run_clustering(df):
    exp_clf = setup(df)
    
    kmeans = create_model('kmeans')
    
    # NOTE: due to a known bug you have to rename .png to .html
    plot_model(kmeans, plot='cluster', save='results/') # Plot clusters using PCA (2D)
    plot_model(kmeans, plot='tsne', save='results/') # Plot clusters using t-SNE (3D)
    plot_model(kmeans, plot='distribution', save='results/')


def main(filename):
    df = load_data(filename)
    
    df = preprocess_data(df)
    
    run_clustering(df)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clustering analysis using PyCaret.")
    parser.add_argument("-N", "--filename", type=str, help="Path to the CSV file containing data.")
    args = parser.parse_args()
    
    if args.filename:
        main(args.filename)
    else:
        print("Please provide a filename using -N or --filename argument.")

"""
Usage instructions:

> python eda/clustering.py -N token_data.csv
    where token_data.csv is a file existing inside data/
"""