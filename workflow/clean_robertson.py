"""
Purpose:
Clean and standardize domain names from Ronald Robertson's list of domains.
Processes raw domain data to extract and normalize domain names by converting
to lowercase and removing non-news, government, and education domains.

Inputs:
- TSV file containing domain data with columns "domain" and "news_is_news"

Outputs:
- CSV file containing cleaned domain names in a single "domain" column

Example:
python clean_robertson.py data/raw/robertson_domains.tsv data/processed/robertson_cleaned.csv
"""

import pandas as pd
import sys
import utils

input_file = sys.argv[1]
output_file = sys.argv[-1]

domains_to_remove = set(["gov", "edu"])

robertson_df = pd.read_csv(input_file, sep="\t", usecols=["domain", "news_is_news"])

robertson_df = robertson_df[robertson_df.news_is_news.notna()].copy()
print(f"{len(robertson_df)} rows after dropping missing values.")

robertson_df["is_news"] = robertson_df.news_is_news.astype(int)
robertson_df = robertson_df[robertson_df.is_news == 1][["domain"]].copy()
print(
    f"{len(robertson_df)} rows after dropping non-news domains based on news_is_news column."
)

robertson_df["domain"] = robertson_df["domain"].str.lower()

robertson_df["suffix"] = robertson_df.domain.apply(utils.extract_suffix)
robertson_df = robertson_df[~robertson_df["suffix"].isin(domains_to_remove)][["domain"]]
print(f"{len(robertson_df)} rows after removing government and education domains.")

robertson_df.drop_duplicates(inplace=True)
print(f"{len(robertson_df)} rows after dropping duplicates.")

robertson_df = robertson_df[
    ~robertson_df["domain"].isin(utils.list_of_domains_to_remove)
][["domain"]]
print(f"{len(robertson_df)} rows after removing non-news domains.")

robertson_df.to_csv(output_file, index=False)
