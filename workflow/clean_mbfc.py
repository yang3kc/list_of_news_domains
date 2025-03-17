"""
Purpose:
Clean and standardize domain names from Media Bias/Fact Check (MBFC) data.
Processes raw MBFC data to extract and normalize domain names by removing paths,
converting to lowercase, and standardizing formatting.

Inputs:
- CSV file containing MBFC source data with columns "source" and "domain"

Outputs:
- CSV file containing cleaned domain names in a single "domain" column

Example:
python clean_mbfc.py data/raw/mbfc.csv data/processed/mbfc_cleaned.csv
"""

import pandas as pd
import sys
import utils

input_file = sys.argv[1]
output_file = sys.argv[-1]

domains_to_remove = set(["gov", "edu"])

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

# Remove government and education domains
mbfc_df["suffix"] = mbfc_df.domain.apply(utils.extract_suffix)
mbfc_df = mbfc_df[~mbfc_df["suffix"].isin(domains_to_remove)][["domain"]]
print(f"{len(mbfc_df)} rows after removing government and education domains.")

mbfc_df.drop_duplicates(inplace=True)
print(f"{len(mbfc_df)} rows after dropping duplicates.")

mbfc_df = mbfc_df[~mbfc_df["domain"].isin(utils.list_of_domains_to_remove)][["domain"]]
print(f"{len(mbfc_df)} rows after removing non-news domains.")

mbfc_df.to_csv(output_file, index=False)
