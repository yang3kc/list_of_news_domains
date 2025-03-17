"""
Purpose:
Clean and standardize domain names from NewsGuard data.
Processes raw NewsGuard data to extract and normalize domain names by converting
to lowercase and removing duplicates.

Inputs:
- CSV file containing NewsGuard source data with column "Domain"
- Dataset name (e.g., "newsguard")
- Output file path

Outputs:
- CSV file containing cleaned domain names in "domain" column and "dataset" column
  identifying the source dataset

Example:
python clean_newsguard.py data/raw/newsguard.csv newsguard data/processed/newsguard_cleaned.csv
"""

import pandas as pd
import sys

input_file = sys.argv[1]
dataset = sys.argv[2]
output_file = sys.argv[-1]

newsguard_df = pd.read_csv(input_file, usecols=["Domain"])
print(f"Load {newsguard_df.shape[0]} rows from {input_file}.")

newsguard_df.rename(columns={"Domain": "domain"}, inplace=True)
newsguard_df["domain"] = newsguard_df.domain.str.lower()

newsguard_df.dropna(inplace=True)
print(f"{len(newsguard_df)} rows after dropping missing values.")

newsguard_df.drop_duplicates(inplace=True)
print(f"{len(newsguard_df)} rows after dropping duplicates.")

newsguard_df["dataset"] = dataset

newsguard_df.to_csv(output_file, index=False)
