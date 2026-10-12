"""List trucking companies added to the FMCSA register in the last N days.

Run:  APIFY_TOKEN=... python fmcsa-carriers/new_carriers.py TX 2
Cost: about $3.00 per 1,000 carriers on the Apify free plan.
"""
import csv
import os
import sys

from apify_client import ApifyClient

state = sys.argv[1] if len(sys.argv) > 1 else "TX"
days = sys.argv[2] if len(sys.argv) > 2 else "2"

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("solidfetch/fmcsa-carriers").call(
    run_input={
        "newCarriersSince": f"{days} days",
        "states": [state],
        "authorizedForHireOnly": True,
        "maxItems": 200,
    }
)

fields = ["dotNumber", "mcNumber", "legalName", "phone", "email", "physicalCity", "physicalState", "powerUnits", "addDate"]
with open("new_carriers.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    writer.writeheader()
    for carrier in client.dataset(run["defaultDatasetId"]).iterate_items():
        writer.writerow(carrier)
print("saved new_carriers.csv")
