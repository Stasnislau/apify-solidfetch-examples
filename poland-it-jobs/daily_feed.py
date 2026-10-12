"""Polish IT jobs from solid.jobs, filtered, with salaries in PLN per month.

Run:  APIFY_TOKEN=... python poland-it-jobs/daily_feed.py
To get only new or changed offers, save this input as a task in Apify Console, turn on
"Only new or changed since the last run" and add a schedule.
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("solidfetch/poland-it-jobs").call(
    run_input={
        "keywords": ["Python"],
        "cities": ["Warsaw"],
        "contractTypes": ["B2B"],
        "minSalaryPln": 20000,
        "publishedWithinDays": 14,
        "maxItems": 100,
    }
)

for job in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(job["title"], "|", job["company"], "|", job.get("salaryPlnMonthlyMax"), "PLN/month |", job["url"])
