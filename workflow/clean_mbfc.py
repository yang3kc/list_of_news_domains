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
from urllib.parse import urlparse
import tldextract

input_file = sys.argv[1]
output_file = sys.argv[-1]

mbfc_df = pd.read_csv(input_file, usecols=["source", "domain"])
print(f"Load {mbfc_df.shape[0]} rows from {input_file}.")

mbfc_df.dropna(inplace=True)
print(f"{len(mbfc_df)} rows after dropping missing values.")


def has_path(url):
    """
    Check if a URL has a path component.

    Args:
        url (str): URL string to check

    Returns:
        bool: True if URL has a non-empty path, False otherwise
    """
    parsed_url = urlparse(url)
    path = parsed_url.path.replace("/", "")
    return path != ""


def extract_suffix(url):
    """
    Extract the top-level domain suffix from a URL.

    Args:
        url (str): URL string to extract suffix from

    Returns:
        str: The top-level domain suffix (e.g. 'com', 'org', 'co.uk')
    """
    extracted = tldextract.extract(url)
    suffix = extracted.suffix
    return suffix


# Remove URLs with paths
# We only want the instances where the whole domain belongs to a news outlet
mbfc_df["has_path"] = mbfc_df["source"].apply(has_path)
mbfc_df = mbfc_df[~mbfc_df["has_path"]][["domain"]]
print(f"{len(mbfc_df)} rows after removing URLs with paths.")

mbfc_df["domain"] = mbfc_df.domain.str.lower()
mbfc_df["domain"] = mbfc_df.domain.str.replace("/", "")

# Remove government and education domains
mbfc_df["suffix"] = mbfc_df.domain.apply(extract_suffix)
mbfc_df = mbfc_df[~mbfc_df["suffix"].isin(set(["gov", "edu"]))][["domain"]]
print(f"{len(mbfc_df)} rows after removing government and education domains.")

mbfc_df.drop_duplicates(inplace=True)
print(f"{len(mbfc_df)} rows after dropping duplicates.")

mbfc_df.to_csv(output_file, index=False)
