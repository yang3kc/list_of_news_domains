"""
Purpose:
Clean and standardize domain names from Le Quere et al. (2022) data.
Processes raw Le Quere data to extract and normalize domain names by removing paths,
converting to lowercase, and removing duplicates.

Inputs:
- CSV file containing Le Quere source data with "WebsiteUrl" column
- String identifier for the dataset
- Output file path

Outputs:
- CSV file containing cleaned domain names with "domain" and "dataset" columns
  identifying the source dataset

Example:
python clean_le_quere.py data/raw/le_quere.csv le_quere data/processed/le_quere_cleaned.csv
"""

import pandas as pd
import sys

input_file = sys.argv[1]
dataset = sys.argv[2]
output_file = sys.argv[-1]

le_quere_df = pd.read_csv(input_file, usecols=["WebsiteUrl"])
print(f"Load {le_quere_df.shape[0]} rows from {input_file}.")

le_quere_df.rename(columns={"WebsiteUrl": "domain"}, inplace=True)
le_quere_df["domain"] = le_quere_df.domain.str.lower()

le_quere_df.dropna(inplace=True)
print(f"{len(le_quere_df)} rows after dropping missing values.")

le_quere_df = le_quere_df[~le_quere_df["domain"].str.contains("/")][["domain"]]
print(f"{len(le_quere_df)} rows after removing URLs with paths.")

le_quere_df.drop_duplicates(inplace=True)
print(f"{len(le_quere_df)} rows after dropping duplicates.")

le_quere_df["dataset"] = dataset
le_quere_df.to_csv(output_file, index=False)
