"""
Purpose:
Clean and standardize domain names from Media Cloud US sources data.
Processes raw Media Cloud data to extract and normalize domain names by removing paths,
converting to lowercase, and removing duplicates.

Inputs:
- Parquet file containing Media Cloud source data with "name" column
- String identifier for the dataset
- Output file path

Outputs:
- CSV file containing cleaned domain names with "domain" and "dataset" columns
  identifying the source dataset

Example:
python clean_media_cloud.py data/raw/media_cloud_us_sources.parquet media_cloud data/processed/media_cloud_cleaned.csv
"""

import pandas as pd
import sys

input_file = sys.argv[1]
dataset = sys.argv[2]
output_file = sys.argv[-1]

media_cloud_df_raw = pd.read_parquet(input_file)

media_cloud_df = media_cloud_df_raw[["name"]].copy()

media_cloud_df.rename(columns={"name": "domain"}, inplace=True)

media_cloud_df.dropna(inplace=True)
print(f"{len(media_cloud_df)} rows after dropping missing values.")

media_cloud_df["domain"] = media_cloud_df["domain"].str.lower()

media_cloud_df = media_cloud_df[~media_cloud_df["domain"].str.contains("/")][["domain"]]
print(f"{len(media_cloud_df)} rows after removing URLs with paths.")

media_cloud_df.drop_duplicates(inplace=True)
print(f"{len(media_cloud_df)} rows after dropping duplicates.")

media_cloud_df["dataset"] = dataset
media_cloud_df.to_csv(output_file, index=False)
