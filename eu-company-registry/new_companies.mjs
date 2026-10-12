// New companies registered in Poland (KRS) since yesterday. Schedule it daily.
// Run:  APIFY_TOKEN=... node eu-company-registry/new_companies.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('solidfetch/eu-company-registry').call({
    mode: 'newSince',
    countries: ['PL'],
    since: '1 day',
    onlyActive: true,
    maxItems: 500,
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const c of items) {
    console.log([c.registeredAt, c.registryId, c.name, c.legalForm, c.address?.city ?? ''].join(' | '));
}
