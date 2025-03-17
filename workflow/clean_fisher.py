"""
Purpose:
Clean and standardize domain names from Fisher et al. (2020) data.
Processes raw Fisher data to extract and normalize domain names by removing paths,
converting to lowercase, and removing duplicates.

Inputs:
- CSV file containing Fisher source data with "domain" column
- String identifier for the dataset
- Output file path

Outputs:
- CSV file containing cleaned domain names with "domain" and "dataset" columns
  identifying the source dataset

Example:
python clean_fisher.py data/raw/fisher.csv fisher data/processed/fisher_cleaned.csv
"""

import pandas as pd
import sys

input_file = sys.argv[1]
dataset = sys.argv[2]
output_file = sys.argv[-1]

fisher_df = pd.read_csv(input_file, usecols=["domain"])
print(f"Load {fisher_df.shape[0]} rows from {input_file}.")

fisher_df.dropna(inplace=True)
print(f"{len(fisher_df)} rows after dropping missing values.")

fisher_df["domain"] = fisher_df.domain.str.lower()
fisher_df["domain"] = fisher_df.domain.str.replace("/", "")

fisher_df.drop_duplicates(inplace=True)
print(f"{len(fisher_df)} rows after dropping duplicates.")

fisher_df["dataset"] = dataset
fisher_df.to_csv(output_file, index=False)
