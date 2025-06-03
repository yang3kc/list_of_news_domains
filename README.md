# List of News Domains

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15073918.svg)](https://doi.org/10.5281/zenodo.15073918)

This repository compiles a canonical list of U.S. news domains from a variety of existing datasets. Researchers can use the list for studies on news consumption, media bias and related topics.

## Quick start

The latest version of the list is available on the [releases page](https://github.com/yang3kc/list_of_news_domains/releases) or directly in [data/output/news_domains.csv](data/output/news_domains.csv).

## Repository structure

```
.
├── data/          # raw input lists and final output
├── notebooks/     # Jupyter notebooks for exploration
├── workflow/      # cleaning scripts and Snakemake pipeline
└── README.md      # project overview (this file)
```

### Data
- `data/raw_data/` – original source files and exclusion lists
- `data/output/` – the compiled list of domains

A full description of each source can be found in [data/raw_data/README.md](data/raw_data/README.md).

## Running the pipeline

The build process is managed with [Snakemake](https://snakemake.readthedocs.io). To regenerate `news_domains.csv`:

1. Install the dependencies in a Python environment with `pandas` and `tldextract`.
2. From the repository root, run `snakemake -j 1`.

Each rule cleans one input dataset and writes a standardized CSV. The cleaned files are concatenated, deduplicated and filtered with the exclusion lists to produce the final output.

### Adding new data sources

Cleaning scripts follow a simple pattern (see `workflow/clean_mbfc.py` for an example). To include another list:
1. Write a new `clean_*.py` script that outputs a single-column CSV with a `domain` column.
2. Add a rule to `workflow/Snakefile` and include the resulting file in the `combine_cleaned_data` step.

## Citation

If you use this list, please cite:

```bibtex
@dataset{yang2025newsdomains,
  author       = {Yang, Kai-Cheng},
  title        = {A list of news domains},
  month        = mar,
  year         = {2025},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.15073918},
  url          = {https://doi.org/10.5281/zenodo.15073918},
}
```
