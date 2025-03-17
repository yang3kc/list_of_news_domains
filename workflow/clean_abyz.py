"""
Purpose:
Clean and standardize domain names from ABYZ data.
Processes raw ABYZ data to extract and normalize domain names by converting to lowercase
and removing duplicates.

Inputs:
- CSV file containing ABYZ source data with "domain" column

Outputs:
- CSV file containing cleaned domain names in a single "domain" column

Example:
python clean_abyz.py data/raw/abyz.csv data/processed/abyz_cleaned.csv
"""

import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[-1]

abyz_df = pd.read_csv(input_file, usecols=["domain"])
print(f"Load {abyz_df.shape[0]} rows from {input_file}.")

abyz_df.dropna(inplace=True)
print(f"{len(abyz_df)} rows after dropping missing values.")

abyz_df["domain"] = abyz_df.domain.str.lower()

abyz_df.drop_duplicates(inplace=True)
print(f"{len(abyz_df)} rows after dropping duplicates.")

abyz_df.to_csv(output_file, index=False)
