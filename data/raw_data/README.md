# Introduction

This folder stores the raw data for the project.

# Data sources

In this project, we consider the following data sources:

## NewsGuard

- [newsguard_20200519.csv](./newsguard_20200519.csv)

NewsGuard is a commercial service that provides a score for the credibility of news websites.
Note that the NewsGuard dataset is proprietary.
Here we use the list of the domains (no ratings) shared by [Buntain et al.](https://osf.io/wtf9y/).

## MBFC

- [mbfc_ratings.csv](./mbfc_ratings.csv)

MBFC (Media Bias/Fact Check) provides a rating for the credibility of news websites.
We collected the data from its [website](https://mediabiasfactcheck.com).

## Robertson

- [robertson_domains.tsv](./robertson_domains.tsv)

Ronald Robertson shared a list of news domains at https://github.com/gitronald/domains.
This list contains data from the following sources:
1. [Bakshy et al. (2015)](https://www.science.org/doi/10.1126/science.aaa1160)
2. [Grinberg et al. (2019)](https://www.science.org/doi/10.1126/science.aau2706)
3. [Yin (2018)](https://zenodo.org/records/1345145)
4. [Robertson et al. (2018)](https://dl.acm.org/doi/10.1145/3274417)

Specifically, Robertson et al. (2018) collected the data from the following sources:
1. [AllSides](https://www.allsides.com/media-bias/media-bias-ratings)
2. [Mitchell et al. (2014)](https://assets.pewresearch.org/wp-content/uploads/sites/13/2014/10/Political-Polarization-and-Media-Habits-FINAL-REPORT-7-27-15.pdf)
3. [Budak et al. (2016)](https://academic.oup.com/poq/article/80/S1/250/2223443)
4. [Bakshy et al. (2015)](https://www.science.org/doi/10.1126/science.aaa1160)

Since not all the domains are news domains, Robertson further provide a `news` label based on the definition of Bakshy et al. (2015), Grinberg et al. (2019), and Yin (2018).

## Hohenberg

- [hohenberg.csv](./hohenberg.csv)

Hohenberg et al. (2021) shared a list of news domains at https://github.com/ercexpo/us-news-domains.

## Le Quéré

- [le_querre.csv](./le_querre.csv)

Le Quéré et al. (2022) shared a list of news domains at https://github.com/sTechLab/local-news-dataset.

## Fisher

- [fisher.csv](./fisher.csv)

Fisher et al. (2022) shared a list of news domains at https://osf.io/hwuxf.
Their list was derived from multiple sources, including Yin (2018).

## Horne

- [horne.csv](./horne.csv)

Horne et al. (2022) shared a list of local news outlets at https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/GFE66K.

## ABYZ

- [abyz.csv](./abyz.csv)

abyznewslinks.com provides a list of newspapers and news media in the U.S., classifying them as either local or national.
We obtained the data from its website.

## Media Cloud

- [media_cloud_us_sources_20250326.parquet](./media_cloud_us_sources_20250326.parquet)

Media Cloud tracks the news sources across the world.
We obtained the list of news sources from the U.S.
See their [instructions](https://github.com/mediacloud/api-tutorial-notebooks/blob/main/MC04%20-%20directory.ipynb) for how to access the data through their API.

## Northwestern Local News

- [nwu_local_news_sites.csv](./nwu_local_news_sites.csv)

[Northwestern Local News Initiative](https://localnewsinitiative.northwestern.edu) provides a list of local news outlets in the U.S.
We obtained the data by contacting the team and extracted the list of local news outlets.

## Exclusion list

After cleaning and combining all the list above, we manually identified some domains that should not be included in the final list.

### Government and education domains

- [gov_edu_domains_to_exclude.csv](./gov_edu_domains_to_exclude.csv)

This list includes domains that end with `.edu` or `.gov`.
We manually annotate the list and remove the ones that are not news domains.
Specifically, we remove all government domains and official university domains.

Note that some newspapers operated by the universities share the same top domains as the official domains, but with different subdomains (e.g., collegian.psu.edu).
These newspapers are considered as news domains and are included in the final list.

### Non-news domains

- [domain_to_exclude.csv](./domain_to_exclude.csv)

We merged the combined list with the [Tranco list](https://tranco-list.eu/), which provides the rank of the domains based on their popularity.
We focus on the most popular domains and remove those that shouldn't not be included in the final list.
They are:

- search engines (e.g., google.com)
- social media domains (e.g., facebook.com, twitter.com)
- website builders (e.g., wordpress.com, wix.com)
- blogs (e.g., medium.com)
- etc.
