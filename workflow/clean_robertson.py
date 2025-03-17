"""
Purpose:
Clean and standardize domain names from Ronald Robertson's list of domains.
Processes raw domain data to extract and normalize domain names by converting
to lowercase, removing non-news domains, and removing duplicates.

Inputs:
- TSV file containing domain data with columns "domain" and "news_is_news"
- String identifier for the dataset

Outputs:
- CSV file containing cleaned domain names with "domain" and "dataset" columns

Example:
python clean_robertson.py data/raw/robertson_domains.tsv robertson data/processed/robertson_cleaned.csv
"""

import pandas as pd
import sys

input_file = sys.argv[1]
dataset = sys.argv[2]
output_file = sys.argv[-1]

robertson_df = pd.read_csv(input_file, sep="\t", usecols=["domain", "news_is_news"])

robertson_df = robertson_df[robertson_df.news_is_news.notna()].copy()
print(f"{len(robertson_df)} rows after dropping missing values.")

robertson_df["is_news"] = robertson_df.news_is_news.astype(int)
robertson_df = robertson_df[robertson_df.is_news == 1][["domain"]].copy()
print(
    f"{len(robertson_df)} rows after dropping non-news domains based on news_is_news column."
)

robertson_df["domain"] = robertson_df["domain"].str.lower()

robertson_df.drop_duplicates(inplace=True)
print(f"{len(robertson_df)} rows after dropping duplicates.")

robertson_df["dataset"] = dataset
robertson_df.to_csv(output_file, index=False)
