# portal-api

The portal's HTTP API, as transport-free handlers: `health()` and `quote(request)`. It is the only component in
this repository that is deployed; see [docs/runbook-portal-api.md](../../docs/runbook-portal-api.md).

Depends on `pricing` and `notifications`, through their public API only.

Owner: team-portal.
