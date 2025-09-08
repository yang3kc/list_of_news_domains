# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository compiles a canonical list of U.S. news domains from multiple existing datasets using a Snakemake pipeline. The final output is `data/output/news_domains.csv` containing deduplicated and filtered news domains.

## Core Commands

### Running the Pipeline
```bash
# Run the complete Snakemake pipeline from repository root
snakemake -j 1
```

### Working with Data Files
```bash
# View parquet files (limit to 10 rows)
parquet-tools show -n 10 data/raw_data/media_cloud_us_sources_20250326.parquet

# Inspect parquet schema
parquet-tools inspect data/raw_data/media_cloud_us_sources_20250326.parquet
```

## Architecture

### Data Pipeline Structure
The pipeline follows a three-stage architecture:

1. **Cleaning Stage** (`clean_*.py` scripts): Each data source has its own cleaning script that:
   - Removes NaN values and URLs with paths
   - Converts domains to lowercase
   - Removes duplicates
   - Outputs standardized CSV with `domain` and `dataset` columns

2. **Aggregation Stage**: 
   - `concat_csv.py`: Combines all cleaned files
   - `gen_unique_data.py`: Deduplicates combined data
   - `merge_with_tranco.py`: Adds popularity rankings

3. **Filtering Stage**: `filter_domains.py` removes non-news domains using exclusion lists for government, education, and manually identified domains

### Key Components

- **`workflow/utils.py`**: Core utilities for URL parsing and domain extraction using `tldextract`
- **`workflow/Snakefile`**: Pipeline orchestration defining all rules and dependencies
- **Data Sources**: 11 different news domain lists processed through individual cleaning scripts
- **Exclusion Lists**: Manual curation of non-news domains to filter out

### File Organization
```
workflow/
├── clean_*.py          # Individual cleaning scripts (11 sources)
├── concat_csv.py       # Combines cleaned files
├── gen_unique_data.py  # Deduplication
├── filter_domains.py   # Final filtering
├── utils.py           # Shared utilities
└── Snakefile          # Pipeline definition
```

## Dependencies

- `pandas`: Data manipulation
- `tldextract`: Domain extraction and parsing
- `snakemake`: Workflow management

## Adding New Data Sources

To include a new data source:
1. Create `clean_[source].py` following the pattern in `clean_mbfc.py`
2. Add a rule to `Snakefile`
3. Include the cleaned file in the `combine_cleaned_data` rule input list

The cleaning script should output a CSV with columns `domain` and `dataset`.