# tv-portal

A disposable multi-component sandbox for TandemVelocity soak runs. Nothing here is production code; the
repository is expected to accumulate throwaway branches and pull requests.

| Component | Path | Kind | Deployed |
|---|---|---|---|
| portal-api | `services/portal-api/` | service | yes, to `production` |
| pricing | `packages/pricing/` | library | inside portal-api |
| notifications | `packages/notifications/` | library | no |

Run every component's tests with `pytest -q` from the repository root. Read
[CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request, and [docs/architecture.md](docs/architecture.md)
for how the components fit together.
