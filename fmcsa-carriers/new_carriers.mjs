// List trucking companies added to the FMCSA register in the last N days.
// Run:  APIFY_TOKEN=... node fmcsa-carriers/new_carriers.mjs TX 2
import { ApifyClient } from 'apify-client';

const [state = 'TX', days = '2'] = process.argv.slice(2);
const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor('solidfetch/fmcsa-carriers').call({
    newCarriersSince: `${days} days`,
    states: [state],
    authorizedForHireOnly: true,
    maxItems: 200,
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const c of items) {
    console.log([c.dotNumber, c.legalName, c.phone, c.email ?? '', c.powerUnits ?? ''].join(' | '));
}
