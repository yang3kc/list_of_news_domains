"""
Purpose:
Clean and standardize domain names from Hohenberg et al. (2023) data.
Processes raw Hohenberg data to extract and normalize domain names by removing paths,
converting to lowercase, and removing duplicates.

Inputs:
- CSV file containing Hohenberg source data with "domain" column
- String identifier for the dataset
- Output file path

Outputs:
- CSV file containing cleaned domain names with "domain" and "dataset" columns
  identifying the source dataset

Example:
python clean_hohenberg.py data/raw/hohenberg.csv hohenberg data/processed/hohenberg_cleaned.csv
"""

import pandas as pd
import sys

input_file = sys.argv[1]
dataset = sys.argv[2]
output_file = sys.argv[-1]

hohenberg_df = pd.read_csv(input_file, usecols=["domain"])
print(f"Load {hohenberg_df.shape[0]} rows from {input_file}.")

hohenberg_df = hohenberg_df[hohenberg_df.domain.notna()][["domain"]]
print(f"{len(hohenberg_df)} rows after dropping missing values.")

hohenberg_df["domain"] = hohenberg_df.domain.str.lower()

hohenberg_df = hohenberg_df[~hohenberg_df["domain"].str.contains("/")][["domain"]]
print(f"{len(hohenberg_df)} rows after removing URLs with paths.")

hohenberg_df.drop_duplicates(inplace=True)
print(f"{len(hohenberg_df)} rows after dropping duplicates.")

hohenberg_df["dataset"] = dataset
hohenberg_df.to_csv(output_file, index=False)
