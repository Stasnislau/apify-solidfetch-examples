"""Get only the Google ads a competitor started since the previous run. Schedule it daily.

Run:  APIFY_TOKEN=... python google-ads-transparency/new_ads_daily.py nike.com
The first run saves every current ad as a baseline; later runs return only new ads, and you pay only for those.
"""
import os
import sys

from apify_client import ApifyClient

domain = sys.argv[1] if len(sys.argv) > 1 else "nike.com"
client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("solidfetch/google-ads-transparency-scraper").call(
    run_input={"domains": [domain], "onlyNewSinceLastRun": True, "monitorName": f"new-ads-{domain}", "maxAds": 200}
)

new_ads = list(client.dataset(run["defaultDatasetId"]).iterate_items())
print(f"{len(new_ads)} new ads for {domain}")
for ad in new_ads:
    print(ad["firstShown"], ad["format"], ad["advertiserName"], ad["transparencyUrl"])
