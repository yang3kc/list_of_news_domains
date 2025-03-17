"""
Purpose:
Concatenate multiple cleaned domain name CSV files into a single file.
Takes multiple input CSV files containing cleaned domain names and combines them
into a single output CSV file.

Inputs:
- Multiple CSV files containing cleaned domain names in "domain" column

Outputs:
- Single CSV file containing combined domain names from all input files

Example:
python concat_csv.py data/processed/newsguard_cleaned.csv data/processed/mbfc_cleaned.csv output.csv
"""

import pandas as pd
import sys

input_files = sys.argv[1:-1]
output_file = sys.argv[-1]

df = pd.concat([pd.read_csv(f) for f in input_files])
df.to_csv(output_file, index=False)
