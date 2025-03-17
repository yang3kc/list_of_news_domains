"""
Purpose:
Merge domain list with Tranco rankings to filter and rank domains.
Takes a list of unique domains and joins it with Tranco top 1M domains list
to identify which domains are popular and their relative rankings.

Inputs:
- CSV file containing unique domain names with "domain" column
- CSV file containing Tranco rankings with "domain" and "rank" columns
- Output file path

Outputs:
- CSV file containing matched domains with their Tranco ranks, sorted by rank

Example:
python merge_with_tranco.py data/processed/combined_unique.csv data/raw/tranco_list.csv data/processed/domain_with_rank.csv
"""

import pandas as pd
import sys

domain_list_file = sys.argv[1]
tranco_list_file = sys.argv[2]
output_file = sys.argv[-1]

domain_list = pd.read_csv(domain_list_file, usecols=["domain"])
tranco_list = pd.read_csv(tranco_list_file, usecols=["domain", "rank"])

merged_df = pd.merge(domain_list, tranco_list, on="domain", how="inner")

merged_df.sort_values(by="rank", inplace=True)

merged_df.to_csv(output_file, index=False)
