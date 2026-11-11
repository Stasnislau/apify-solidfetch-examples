---
name: solidfetch-data-lookups
description: Look up business data through seven pay-per-result Apify actors. Use when the user asks for new US trucking companies or a carrier check by USDOT/MC number (FMCSA), a company check by VAT, NIP, KRS, orgnr, IČO or SIREN, new Polish companies, the Google ads a competitor runs or which domains advertise on Google, real-user Core Web Vitals of a site against competitors, Google Trends movement for keywords, Polish IT jobs with salaries, or local businesses with a phone and no website.
---

# solidfetch data lookups

Each task below runs one actor on the Apify platform through the official `apify-client` package and saves the
results to a CSV file or prints them. The scripts are in this repository; every one is a short file you can read in a
minute.

## Requirements

- `APIFY_TOKEN` in the environment (Apify Console → Settings → Integrations). The scripts read it from the
  environment and never write it anywhere.
- Python 3 with `pip install -r requirements.txt`, or Node 18+ with `npm install` for the `.mjs` files.

## Network calls

The scripts talk only to `api.apify.com`, through `apify-client`. The actors themselves read official open data
(FMCSA Company Census File, national company registers of Poland, Norway, Finland, Czechia, Slovakia and France plus
GLEIF, the Google Ads Transparency Center, the Chrome UX Report API, Google Trends, the solid.jobs public API, Overture
Maps). Nothing else is called.

## Cost

The actors charge per result to the Apify account that owns `APIFY_TOKEN`. Prices below are the Apify free-plan prices
on 11 Nov 2026; the actor page always has the current ones. Each run also has a start fee of $0.00005
($0.001 for local business leads).

| Actor | Charged per | Price |
|---|---|---|
| `solidfetch/fmcsa-carriers` | carrier | $0.003 |
| `solidfetch/eu-company-registry` | company | $0.004 |
| `solidfetch/google-ads-transparency-scraper` | saved ad / checked domain | $0.0015 / $0.006 |
| `solidfetch/crux-competitor-benchmark` | site with data (sites without data are free) | $0.01 |
| `solidfetch/google-trends-monitor` | keyword / trend row | $0.003 / $0.0005 |
| `solidfetch/poland-it-jobs` | job / salary report row | $0.002 / $0.01 |
| `solidfetch/overture-places-leads` | place | $0.003 |

Before a run that can return many rows, tell the user the likely cost and keep the `maxItems` in the script.

## Which script to run

| The user wants | Command |
|---|---|
| New trucking companies in a state in the last N days, with phone and e-mail | `python fmcsa-carriers/new_carriers.py TX 2` (or `node fmcsa-carriers/new_carriers.mjs TX 2`) |
| Check carriers by USDOT or MC number | `python fmcsa-carriers/lookup_by_usdot.py 53467 80806` |
| Check companies by VAT, NIP, KRS, orgnr, IČO or SIREN | `python eu-company-registry/bulk_lookup.py PL5260250995 NO923609016MVA` |
| Companies registered in Poland since yesterday | `node eu-company-registry/new_companies.mjs` |
| The Google ads a competitor ran in Poland in the last 30 days | `python google-ads-transparency/competitor_ads.py "Advertiser name"` (edit `region` in the script for another country) |
| Only the ads a competitor started since the last run | `python google-ads-transparency/new_ads_daily.py domain.com` |
| Which domains from a list advertise on Google | `python google-ads-transparency/check_domains.py domains.txt` (one domain per line) |
| Core Web Vitals of a site against competitors | `python crux-competitor-benchmark/compare_competitors.py site.com rival1.com rival2.com` |
| Google Trends keywords that moved since the last run | `python google-trends-monitor/keyword_monitor.py "keyword one" "keyword two"` |
| Polish IT jobs with salaries in PLN per month | `python poland-it-jobs/daily_feed.py` |
| Businesses with a phone and no website in a city | `python overture-places-leads/no_website_leads.py PL Warsaw dentist` |

Run the commands from the repository root. `new_carriers.py` and `no_website_leads.py` save a CSV in the current folder and say so; the other scripts print their rows.

## Errors

- A missing `APIFY_TOKEN` stops a Python script with `KeyError: 'APIFY_TOKEN'` and a Node script with an Apify authentication error: ask the user to set it.
- A failed actor run raises an error from `apify-client` with the run ID; show it to the user. The run log is in
  Apify Console → Runs.
