# Portal architecture

One repository, three components.

| Component | Path | Kind | Owner | Depends on |
|---|---|---|---|---|
| portal-api | `services/portal-api/` | service | team-portal | pricing, notifications |
| pricing | `packages/pricing/` | library | team-billing | nothing |
| notifications | `packages/notifications/` | library | team-comms | nothing |

## How a quote is priced

`portal_api.handlers.quote` validates the request, then calls `pricing` in this order:

1. `line_total(unit_price, quantity)` per item, summed into the subtotal;
2. `coupon_percent(code)` when the request names a coupon;
3. `apply_discount(subtotal, percent)`;
4. `add_tax(discounted, region)`, using `pricing.tax.RATES`.

A region or coupon the tables do not contain currently raises `KeyError`, which the handler boundary turns into
a 500. CONTRIBUTING.md rule 4 says it should be a 4xx.

## Boundaries

- `pricing` and `notifications` know nothing about HTTP or about each other.
- `portal-api` imports only the names in `pricing.__all__` and `notifications.__all__` (CONTRIBUTING.md, rule 2).

## Production

Only `portal-api` is deployed: environment `production`, AWS region `us-east-2`.

- **Deployed revision:** SSM parameter `/tandemvelocity/sandbox/portal-api/deployment`, written by the release
  pipeline with `{revision, artifact, environment, deployed_at}`.
- **Logs:** CloudWatch log group `/tandemvelocity/sandbox/portal-api`.
- **Alarms:** `tandemvelocity-sandbox-portal-api-errors` (5xx count) and
  `tandemvelocity-sandbox-portal-api-latency` (p95 latency), both in namespace `TandemVelocity/Sandbox`.
