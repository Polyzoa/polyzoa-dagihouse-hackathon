import argparse
import os
import pandas as pd
from ydata_profiling import ProfileReport

def main(args):
    if args.filename:
        # Construct paths
        input_file = os.path.join('data', args.filename)
        base_filename = os.path.splitext(args.filename)[0]
        output_folder = 'results'
        output_file = os.path.join(output_folder, f"report_{base_filename}.html")


        # Check if the input file exists
        if not os.path.exists(input_file):
            print(f"Error: The file {input_file} does not exist.")
            return

        df = pd.read_csv(input_file)

        # Generate report
        profile = ProfileReport(df, title=f"Exploratory Data Analysis Report {base_filename}")

        # Save report as HTML
        os.makedirs(output_folder, exist_ok=True)
        profile.to_file(output_file)
        print(f"Report saved successfully to: {output_file}")
    else:
        print("Error: Please provide a filename using -N option.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate EDA report for a CSV file")
    parser.add_argument('-N', '--filename', type=str, help="Name of the CSV file located in the 'data' directory")
    args = parser.parse_args()

    main(args)


"""
Usage instructions:

> python eda/report.py -N token_data.csv
    where token_data.csv is a file existing inside data/
"""