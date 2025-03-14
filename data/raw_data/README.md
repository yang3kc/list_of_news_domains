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