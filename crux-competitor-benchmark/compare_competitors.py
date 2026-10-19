"""Compare real-user Core Web Vitals of your site with competitors (Chrome UX Report data).

Run:  APIFY_TOKEN=... python crux-competitor-benchmark/compare_competitors.py zalando.de aboutyou.de otto.de
Cost: about $0.01 per site with data on the Apify free plan; sites without data are free. No Google API key needed.
"""
import os
import sys

from apify_client import ApifyClient

sites = sys.argv[1:] or ["zalando.de", "aboutyou.de", "otto.de"]
client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("solidfetch/crux-competitor-benchmark").call(run_input={"urls": sites, "formFactor": "PHONE"})

for row in client.dataset(run["defaultDatasetId"]).iterate_items():
    if row.get("error"):
        print(f"{row['input']}: {row['error']}")
        continue
    lcp = row["largest_contentful_paint"]["p75"]
    inp = (row.get("interaction_to_next_paint") or {}).get("p75")
    cls = (row.get("cumulative_layout_shift") or {}).get("p75")
    verdict = {True: "passes", False: "fails", None: "incomplete"}[row["passesCoreWebVitals"]]
    print(f"{row['queried']}: LCP {lcp} ms, INP {inp} ms, CLS {cls}, {verdict} Core Web Vitals")
