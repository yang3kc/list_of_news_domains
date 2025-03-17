# Introduction
This folder stores the scripts for data processing and analysis.

Here, we use [Snakemake](https://snakemake.readthedocs.io/en/stable/) for workflow management.

# Processing steps

## Format

Although different data sources require slightly different preprocessing steps, the common steps include:

1. Remove rows with NaN values
1. Remove URLs with paths (e.g., facebook.com/news, these cases will pose challenge for downstream analyses, so we only keep the domains)
1. Lower the case
1. Remove duplicates
1. Unify domain format

## Non-news domains

To generate the final list, we additionally remove certain non-news domains.

### Government domains

Many government domains, such as whitehouse.gov, are included by one or more sources as "news" domains.
However, we do not consider them as news domains and believe that they should be treated differently.
Therefore, we remove them from the final list.

### Education domains

The official domains of some universities are included by one or more sources as "news" domains.
Similar to the government domains, we do not consider them as news domains and believe that they should be treated differently.
Therefore, we remove them from the final list.

Note that some newspapers operated by the universities share the same top domains as the official domains, but with different subdomains (e.g., collegian.psu.edu).
These newspapers are considered as news domains and are included in the final list.