"""Pull the Google ads a competitor runs, and flag the long-running ones.

Run:  APIFY_TOKEN=... python google-ads-transparency/competitor_ads.py Allegro zalando.pl
Cost: about $1.50 per 1,000 saved ads on the Apify free plan.
"""
import os
import sys

from apify_client import ApifyClient

names = sys.argv[1:] or ["Allegro"]
client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("solidfetch/google-ads-transparency-scraper").call(
    run_input={"advertiserNames": names, "region": "Poland", "shownInLastDays": 30, "maxAds": 100}
)

ads = list(client.dataset(run["defaultDatasetId"]).iterate_items())
ads.sort(key=lambda ad: ad.get("daysShown") or 0, reverse=True)
for ad in ads[:20]:
    print(ad["advertiserName"], ad["format"], ad.get("daysShown"), ad["transparencyUrl"])
