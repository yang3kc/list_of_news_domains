"""
Purpose:
Generate a dataset of unique domain names from the combined cleaned data.
Takes the combined dataset of cleaned domain names from multiple sources and
removes any duplicate domains to create a final unique set.

Inputs:
- CSV file containing combined cleaned data with "domain" column
- Output file path

Outputs:
- CSV file containing unique domain names with "domain" column

Example:
python gen_unique_data.py data/processed/cleaned_combined.csv data/processed/combined_unique.csv
"""

import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[-1]

df = pd.read_csv(input_file, usecols=["domain"])

df.drop_duplicates(subset=["domain"], inplace=True)

df.to_csv(output_file, index=False)
