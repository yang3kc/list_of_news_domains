import pandas as pd
import sys
import utils

DOMAIN_LIST_FILE = sys.argv[1]
SUFFIX_LIST = sys.argv[2].split("_")
OUTPUT_FILE = sys.argv[-1]

suffix_set = set(SUFFIX_LIST)

domain_list_df = pd.read_csv(DOMAIN_LIST_FILE, usecols=["domain"])

domain_list_df["suffix"] = domain_list_df["domain"].apply(utils.extract_suffix)

domain_list_df = domain_list_df[domain_list_df["suffix"].isin(suffix_set)]

domain_list_df.to_csv(OUTPUT_FILE, index=False)
