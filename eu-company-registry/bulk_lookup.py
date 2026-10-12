"""Check companies in bulk by VAT number, NIP, KRS, orgnr, ICO or SIREN.

Run:  APIFY_TOKEN=... python eu-company-registry/bulk_lookup.py PL5260250995 NO923609016MVA FI01120389
Every input gets an outcome in the run report: saved, not found, invalid, ambiguous, skipped or failed.
"""
import os
import sys

from apify_client import ApifyClient

ids = sys.argv[1:] or ["PL5260250995", "NO923609016MVA", "FI01120389"]
client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("solidfetch/eu-company-registry").call(run_input={"mode": "lookup", "ids": ids})

for company in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(company["country"], company["registryId"], company["name"], company["status"], company.get("vatRegistered"))

report = client.key_value_store(run["defaultKeyValueStoreId"]).get_record("RUN_REPORT")
if report:
    print("run report:", report["value"])
