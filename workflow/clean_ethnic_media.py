"""
Purpose:
Clean and standardize domain names from ethnic media data.
Processes raw ethnic media data which contains pre-cleaned domain names.

Inputs:
- CSV file containing ethnic media source data with "domain" column
- String identifier for the dataset (e.g., "ethnic_media")
- Output file path

Outputs:
- CSV file containing domain names with "domain" and "dataset" columns
  identifying the source dataset

Example:
python clean_ethnic_media.py data/raw/ethnic_media_list.csv ethnic_media data/processed/ethnic_media_cleaned.csv
"""

import pandas as pd
import sys

input_file = sys.argv[1]
dataset = sys.argv[2]
output_file = sys.argv[-1]

ethnic_media_df = pd.read_csv(input_file, usecols=["domain"])
print(f"Load {ethnic_media_df.shape[0]} rows from {input_file}.")

ethnic_media_df["dataset"] = dataset

# The dataset has been cleaned already, so no need to further clean it
ethnic_media_df.to_csv(output_file, index=False)
