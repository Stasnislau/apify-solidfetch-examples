"""Track Google Trends interest for your keywords and get only the ones that moved since the last run.

Run:  APIFY_TOKEN=... python google-trends-monitor/keyword_monitor.py "electric bike" "e-scooter"
"""
import os
import sys

from apify_client import ApifyClient

keywords = sys.argv[1:] or ["electric bike", "e-scooter"]
client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("solidfetch/google-trends-monitor").call(
    run_input={"mode": "monitor", "keywords": keywords, "country": "US", "timeframe": "today 3-m", "monitorName": "my-keywords"}
)

for row in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(row)
