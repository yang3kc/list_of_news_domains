import pandas as pd
import sys

FULL_DOMAIN_FILE = sys.argv[1]
DOMAIN_TO_EXCLUDE_FILE = sys.argv[2]
GOV_EDU_DOMAIN_LIST_TO_EXCLUDE = sys.argv[3]
OUTPUT_FILE = sys.argv[-1]

full_domain_df = pd.read_csv(FULL_DOMAIN_FILE)
print(f"Load {FULL_DOMAIN_FILE} with {len(full_domain_df)} rows")

domain_to_exclude_df = pd.read_csv(DOMAIN_TO_EXCLUDE_FILE)
gov_edu_domain_list_to_exclude_df = pd.read_csv(GOV_EDU_DOMAIN_LIST_TO_EXCLUDE)

gov_edu_domain_list_to_exclude_df = gov_edu_domain_list_to_exclude_df[
    gov_edu_domain_list_to_exclude_df["exclude"]
]

domain_to_exclude_set = set(domain_to_exclude_df["domain"]) | set(
    gov_edu_domain_list_to_exclude_df["domain"]
)
print(f"Total number of domains to exclude: {len(domain_to_exclude_set)}")

full_domain_df = full_domain_df[~full_domain_df["domain"].isin(domain_to_exclude_set)]
print(f"After filtering, {len(full_domain_df)} rows left")

full_domain_df.to_csv(OUTPUT_FILE, index=False)
