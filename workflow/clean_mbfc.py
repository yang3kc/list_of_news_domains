"""
Purpose:
Clean and standardize domain names from Media Bias/Fact Check (MBFC) data.
Processes raw MBFC data to extract and normalize domain names by removing paths,
converting to lowercase, and removing duplicates.

Inputs:
- CSV file containing MBFC source data with columns "source" and "domain"
- String identifier for the dataset

Outputs:
- CSV file containing cleaned domain names with "domain" and "dataset" columns

Example:
python clean_mbfc.py data/raw/mbfc.csv mbfc data/processed/mbfc_cleaned.csv
"""

import pandas as pd
import sys
import utils

input_file = sys.argv[1]
dataset = sys.argv[2]
output_file = sys.argv[-1]

mbfc_df = pd.read_csv(input_file, usecols=["source", "domain"])
print(f"Load {mbfc_df.shape[0]} rows from {input_file}.")

mbfc_df.dropna(inplace=True)
print(f"{len(mbfc_df)} rows after dropping missing values.")

# Remove URLs with paths
# We only want the instances where the whole domain belongs to a news outlet
mbfc_df["has_path"] = mbfc_df["source"].apply(utils.has_path)
mbfc_df = mbfc_df[~mbfc_df["has_path"]][["domain"]]
print(f"{len(mbfc_df)} rows after removing URLs with paths.")

mbfc_df["domain"] = mbfc_df.domain.str.lower()
mbfc_df["domain"] = mbfc_df.domain.str.replace("/", "")

mbfc_df.drop_duplicates(inplace=True)
print(f"{len(mbfc_df)} rows after dropping duplicates.")

mbfc_df["dataset"] = dataset
mbfc_df.to_csv(output_file, index=False)
