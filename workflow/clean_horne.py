"""
Purpose:
Clean and standardize domain names from Horne et al. (2022) data.
Processes raw Horne data to extract and normalize domain names by splitting on hyphens,
converting to lowercase, and removing duplicates.

Inputs:
- CSV file containing Horne source data with "sourcedomain_id" column

Outputs:
- CSV file containing cleaned domain names in a single "domain" column

Example:
python clean_horne.py data/raw/horne.csv data/processed/horne_cleaned.csv
"""

import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[-1]

horne_raw_df = pd.read_csv(input_file, usecols=["sourcedomain_id"])
horne_domains = []
for index, row in horne_raw_df.iterrows():
    horne_domains.append(row["sourcedomain_id"].split("-")[1])
horne_df = pd.DataFrame(horne_domains, columns=["domain"])

horne_df.dropna(inplace=True)
print(f"{len(horne_df)} rows after dropping missing values.")

horne_df["domain"] = horne_df.domain.str.lower()

horne_df.drop_duplicates(inplace=True)
print(f"{len(horne_df)} rows after dropping duplicates.")

horne_df.to_csv(output_file, index=False)
