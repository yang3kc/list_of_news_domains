"""
Purpose:
Clean and standardize domain names from Northwestern Local News (NWU) local news data.
Processes raw NWU local news data which contains pre-cleaned domain names.

Inputs:
- CSV file containing NWU local news source data with "domain" column
- String identifier for the dataset (e.g., "northwestern_local_news")
- Output file path

Outputs:
- CSV file containing domain names with "domain" and "dataset" columns
  identifying the source dataset

Example:
python clean_nwu_local_news.py data/raw/nwu_local_news.csv northwestern_local_news data/processed/nwu_local_news_cleaned.csv
"""

import pandas as pd
import sys

input_file = sys.argv[1]
dataset = sys.argv[2]
output_file = sys.argv[-1]

nwu_local_news_df = pd.read_csv(input_file, usecols=["domain"])
print(f"Load {nwu_local_news_df.shape[0]} rows from {input_file}.")

nwu_local_news_df["dataset"] = dataset

# The dataset has been cleaned already, so no need to further clean it
nwu_local_news_df.to_csv(output_file, index=False)
