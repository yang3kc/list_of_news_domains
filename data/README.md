# Data directory

This folder holds both the original source lists and the final compiled dataset.

```
data/
├── raw_data/   # input lists and exclusion files
└── output/     # news_domains.csv
```

Each data source is documented in [raw_data/README.md](raw_data/README.md). The `output` folder contains the single file `news_domains.csv`, which is produced by the Snakemake pipeline.
