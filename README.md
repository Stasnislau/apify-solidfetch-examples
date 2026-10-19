# Data actor examples: Google Ads Transparency, Core Web Vitals benchmark, FMCSA carriers, EU company registers, Google Trends, Polish IT jobs, local leads

Runnable Python and JavaScript examples for seven pay-per-result actors on the Apify Store. I wrote the actors, so this is my own tool: each actor has a free monthly credit on the Apify free plan, and every example here costs cents.

| Task | Actor | Example |
|---|---|---|
| List new trucking companies (new USDOT numbers) with phone and e-mail | [FMCSA Carrier Lookup](https://apify.com/solidfetch/fmcsa-carriers) | [Python](fmcsa-carriers/new_carriers.py), [JavaScript](fmcsa-carriers/new_carriers.mjs) |
| Check carriers by USDOT or MC number | same | [Python](fmcsa-carriers/lookup_by_usdot.py) |
| Check companies in bulk by VAT, NIP, KRS, orgnr, IČO or SIREN | [EU Company Registry](https://apify.com/solidfetch/eu-company-registry) | [Python](eu-company-registry/bulk_lookup.py) |
| New companies registered in Poland since yesterday | same | [JavaScript](eu-company-registry/new_companies.mjs) |
| See the Google ads a competitor runs, with EU impression ranges | [Google Ads Transparency Scraper](https://apify.com/solidfetch/google-ads-transparency-scraper) | [Python](google-ads-transparency/competitor_ads.py) |
| Get only the Google ads a competitor started since yesterday (schedule daily) | same | [Python](google-ads-transparency/new_ads_daily.py) |
| Check which domains from a list run Google Ads | same | [Python](google-ads-transparency/check_domains.py) |
| Compare real-user Core Web Vitals (LCP, INP, CLS) of your site and competitors | [Core Web Vitals Competitor Benchmark](https://apify.com/solidfetch/crux-competitor-benchmark) | [Python](crux-competitor-benchmark/compare_competitors.py) |
| Track Google Trends interest for your keywords, only what moved | [Google Trends Monitor](https://apify.com/solidfetch/google-trends-monitor) | [Python](google-trends-monitor/keyword_monitor.py) |
| Polish IT jobs from solid.jobs with salaries in PLN per month | [Poland IT Jobs](https://apify.com/solidfetch/poland-it-jobs) | [Python](poland-it-jobs/daily_feed.py) |
| Businesses with a phone and no website in a city | [Local Business Leads from Overture Maps](https://apify.com/solidfetch/overture-places-leads) | [Python](overture-places-leads/no_website_leads.py) |

## Run an example

```bash
pip install -r requirements.txt        # Python examples
npm install                            # JavaScript examples
export APIFY_TOKEN=...                 # Apify Console, Settings, Integrations
python fmcsa-carriers/new_carriers.py TX 2
```

Never commit the token. The examples read it from the environment.

## Guides

- [How to find new trucking companies from FMCSA data](docs/how-to-find-new-trucking-companies.md)

## Data sources

The actors read official open data: the FMCSA Company Census File, the national company registers of Poland, Norway, Finland, Czechia, Slovakia and France plus GLEIF, the Google Ads Transparency Center, the Chrome UX Report API (CC BY 4.0), Google Trends, the solid.jobs public API, and Overture Maps. Each actor page lists its sources and licence terms.

## License

MIT for the code in this repository.
