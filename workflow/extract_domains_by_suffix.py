import sys

import pandas as pd
import utils

DOMAIN_LIST_FILE = sys.argv[1]
SUFFIX_LIST = sys.argv[2].split("_")
OUTPUT_FILE = sys.argv[-1]

suffix_set = set(SUFFIX_LIST)

domain_list_df = pd.read_csv(DOMAIN_LIST_FILE, usecols=["domain"])

print(f"Load {DOMAIN_LIST_FILE} with {len(domain_list_df)} rows")

# Filter out NaN values before applying suffix extraction
domain_list_df = domain_list_df.dropna(subset=["domain"])

print(f"After dropping NaN values, {len(domain_list_df)} rows left")

print("Extracting domains based the following suffixes: ", suffix_set)
domain_list_df["suffix"] = domain_list_df["domain"].apply(utils.extract_suffix)

domain_list_df = domain_list_df[domain_list_df["suffix"].isin(suffix_set)]
print(f"After filtering based on suffixes, {len(domain_list_df)} rows left")

domain_list_df.to_csv(OUTPUT_FILE, index=False)
