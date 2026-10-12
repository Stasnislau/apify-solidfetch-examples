---
title: How to find new trucking companies from FMCSA data
description: Get the trucking companies added to the FMCSA register in the last few days, with phone, e-mail and fleet size. A free query first, then a ready-made option.
---

# How to find new trucking companies from FMCSA data

If you sell insurance, factoring, ELDs, fuel cards or dispatch services, a trucking company is worth most in its first weeks. The FMCSA publishes every registered carrier as open data, so you can list the new ones yourself. This page shows the free way first and a hosted option after it.

## What "new" means in the FMCSA data

The register behind the SAFER website is the Company Census File on data.transportation.gov (dataset `az4n-8mr2`). Each carrier has an `add_date`: the day the record was created or reactivated. A company with a recent `add_date` is a new or returning carrier. The file is refreshed daily and needs no API key.

One change to know about: FMCSA moved registration to a new system called Motus on 14 May 2026, and new USDOT and docket numbers are now issued differently ([CDLLife](https://cdllife.com/2026/fmcsas-may-14-deadline-looms-as-legacy-registration-systems-will-be-retired-and-replaced-by-motus/)). In our test run on 4 October 2026, none of the 2,395 carriers added in the previous 7 days had an MC docket number in the census file. If your list depends on an MC number, check it against the licensing system before you rely on it.

## The free way: one query

This returns the carriers added since 3 October 2026, newest first. `add_date` is stored as text in the form `YYYYMMDD`, so compare it as text.

```bash
curl -G 'https://data.transportation.gov/resource/az4n-8mr2.json' \
  --data-urlencode '$select=dot_number,legal_name,phy_city,phy_state,phone,email_address,power_units,add_date' \
  --data-urlencode "\$where=add_date >= '20261003'" \
  --data-urlencode '$order=add_date DESC' \
  --data-urlencode '$limit=1000'
```

Add `AND phy_state='TX'` to the `$where` for one state. Without an app token the portal throttles heavy use, so register a free app token if you run it on a schedule.

What you still have to handle yourself: records that belong to a private person rather than a company, e-mail addresses that are missing, fleet counts stored as text, and de-duplication between yesterday's run and today's.

## The hosted way

The Apify actor [FMCSA Carrier Lookup](https://apify.com/solidfetch/fmcsa-carriers) runs the same kind of query and adds filters (state, city, fleet size, cargo class, hazmat, e-mail required), leaves the e-mail and street out of rows that look like private persons by default, and returns clean JSON, CSV or Excel. It costs $3.00 per 1,000 carriers on the free plan. I built it, so weigh that. Runnable examples for it are in this repository: [`fmcsa-carriers/new_carriers.py`](https://github.com/Stasnislau/apify-solidfetch-examples/blob/main/fmcsa-carriers/new_carriers.py).

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("solidfetch/fmcsa-carriers").call(
    run_input={"newCarriersSince": "2 days", "states": ["TX"], "authorizedForHireOnly": True}
)
for carrier in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(carrier["legalName"], carrier["phone"], carrier["email"])
```

## Before you call anyone

- Small carriers often file the owner's own mailbox and mobile number. Treat those rows as personal data and check the rules that apply to you for cold calls and e-mail.
- A new record does not prove the company is operating. Many new records never haul a load.
- Check the authority status in FMCSA's own system before you quote or sign anything.

Source of the data: FMCSA Company Census File, https://data.transportation.gov/d/az4n-8mr2.
