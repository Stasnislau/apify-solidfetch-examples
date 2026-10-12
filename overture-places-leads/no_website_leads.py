"""Businesses with a phone number and no website in one city: a web agency lead list.

Run:  APIFY_TOKEN=... python overture-places-leads/no_website_leads.py PL Warsaw dentist
Cost: about $1.50 per 1,000 places on the Apify free plan.
"""
import csv
import os
import sys

from apify_client import ApifyClient

country, city, category = (sys.argv[1:4] + ["PL", "Warsaw", "dentist"][len(sys.argv[1:4]):])
client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("solidfetch/overture-places-leads").call(
    run_input={
        "country": country,
        "city": city,
        "categories": [category],
        "requireWebsite": "false",
        "requirePhone": True,
        "maxPlaces": 500,
    }
)

with open("no_website_leads.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "phone", "address", "city", "facebook"])
    for place in client.dataset(run["defaultDatasetId"]).iterate_items():
        writer.writerow([place["name"], place["phones"][0], place.get("address"), place.get("locality"), (place.get("socials") or [""])[0]])
print("saved no_website_leads.csv")
