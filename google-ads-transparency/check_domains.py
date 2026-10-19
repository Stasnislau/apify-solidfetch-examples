"""Check which domains from a list advertise on Google Ads. One row per domain.

Run:  APIFY_TOKEN=... python google-ads-transparency/check_domains.py domains.txt
domains.txt holds one domain per line.
"""
import os
import sys
from pathlib import Path

from apify_client import ApifyClient

path = Path(sys.argv[1]) if len(sys.argv) > 1 else None
domains = [line.strip() for line in path.read_text().splitlines() if line.strip()] if path else ["nike.com", "allegro.pl"]
client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("solidfetch/google-ads-transparency-scraper").call(run_input={"mode": "domainCheck", "domains": domains})

for row in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(row)
