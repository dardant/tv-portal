# portal-api

The portal's HTTP API, as transport-free handlers: `health()` and `quote(request)`. It is the only component in
this repository that is deployed; see [docs/runbook-portal-api.md](../../docs/runbook-portal-api.md).

Depends on `pricing` and `notifications`, through their public API only.

Owner: team-portal.

## `POST /quote` currencies

Only `USD` and `EUR` are accepted. The request field `currency` is optional and defaults to `"USD"`;
matching is case-insensitive (for example `"usd"` and `"eur"` are accepted). Any other currency is rejected
with a `400` response carrying `{"error": "UNSUPPORTED_CURRENCY", "message": text}`; the basket is not priced.
