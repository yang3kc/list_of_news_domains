"""
Purpose:
Clean and standardize domain names from Hohenberg et al. (2023) data.
Processes raw Hohenberg data to extract and normalize domain names by removing paths,
converting to lowercase, and standardizing formatting.

Inputs:
- CSV file containing Hohenberg source data with "domain" column

Outputs:
- CSV file containing cleaned domain names in a single "domain" column

Example:
python clean_hohenberg.py data/raw/hohenberg.csv data/processed/hohenberg_cleaned.csv
"""

import pandas as pd
import sys
import utils

input_file = sys.argv[1]
output_file = sys.argv[-1]

domains_to_remove = set(["gov", "edu"])

hohenberg_df = pd.read_csv(input_file, usecols=["domain"])
print(f"Load {hohenberg_df.shape[0]} rows from {input_file}.")

hohenberg_df = hohenberg_df[hohenberg_df.domain.notna()][["domain"]]
print(f"{len(hohenberg_df)} rows after dropping missing values.")

hohenberg_df["domain"] = hohenberg_df.domain.str.lower()

hohenberg_df = hohenberg_df[~hohenberg_df["domain"].str.contains("/")][["domain"]]
print(f"{len(hohenberg_df)} rows after removing URLs with paths.")

hohenberg_df.drop_duplicates(inplace=True)
print(f"{len(hohenberg_df)} rows after dropping duplicates.")

hohenberg_df = hohenberg_df[
    ~hohenberg_df["domain"].isin(utils.list_of_domains_to_remove)
][["domain"]]
print(f"{len(hohenberg_df)} rows after removing non-news domains.")

hohenberg_df.to_csv(output_file, index=False)
