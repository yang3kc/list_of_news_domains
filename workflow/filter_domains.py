import sys

import pandas as pd

FULL_DOMAIN_FILE = sys.argv[1]
DOMAIN_TO_EXCLUDE_FILE = sys.argv[2]
SUFFIX_BASED_DOMAINS_TO_EXCLUDE = sys.argv[3]
OUTPUT_FILE = sys.argv[-1]

full_domain_df = pd.read_csv(FULL_DOMAIN_FILE)
print(f"Load {FULL_DOMAIN_FILE} with {len(full_domain_df)} rows")

domain_to_exclude_df = pd.read_csv(DOMAIN_TO_EXCLUDE_FILE)
suffix_based_domains_to_exclude_df = pd.read_csv(SUFFIX_BASED_DOMAINS_TO_EXCLUDE)

suffix_based_domains_to_exclude_df = suffix_based_domains_to_exclude_df[
    suffix_based_domains_to_exclude_df["exclude"]
]
print(
    f"Load {SUFFIX_BASED_DOMAINS_TO_EXCLUDE} with {len(suffix_based_domains_to_exclude_df)} rows"
)

domain_to_exclude_set = set(domain_to_exclude_df["domain"]) | set(
    suffix_based_domains_to_exclude_df["domain"]
)
print(f"Total number of domains to exclude: {len(domain_to_exclude_set)}")

full_domain_df = full_domain_df[~full_domain_df["domain"].isin(domain_to_exclude_set)]
print(f"After filtering, {len(full_domain_df)} rows left")

full_domain_df.to_csv(OUTPUT_FILE, index=False)
