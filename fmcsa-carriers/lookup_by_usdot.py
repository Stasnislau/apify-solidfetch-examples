"""Check a list of carriers by USDOT or MC number (broker vetting).

Run:  APIFY_TOKEN=... python fmcsa-carriers/lookup_by_usdot.py 53467 80806
Numbers that are not in the register are listed in the run summary and are not charged.
"""
import os
import sys

from apify_client import ApifyClient

numbers = sys.argv[1:] or ["53467", "80806"]
client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("solidfetch/fmcsa-carriers").call(run_input={"dotNumbers": numbers})

for c in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(c["dotNumber"], c["legalName"], c["status"], c.get("safetyRating"), c.get("powerUnits"))
