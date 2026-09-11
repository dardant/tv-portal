# Contributing to the portal

Three components share this repository. These rules keep a change to one of them from surprising the owners of
the others. CI enforces rule 1; reviewers enforce the rest.

1. **Every component you touch gets a `CHANGELOG.md` line.** Add it under `## Unreleased` in that component's own
   changelog (`services/portal-api/CHANGELOG.md`, `packages/pricing/CHANGELOG.md`,
   `packages/notifications/CHANGELOG.md`). The `component-changelog` CI job fails a branch that changes a
   component without changing its changelog.
2. **Components depend on each other only through their public API**, the names in the package's `__all__`.
   `portal-api` must not import `pricing.money` or any other module directly. Renaming a public name keeps the old
   name as a deprecated alias for one minor version.
3. **Money is `decimal.Decimal`, rounded half up to the cent** (finance policy FIN-7). New and changed money code
   follows this. `pricing.money` still uses floats and Python's `round`, which rounds half to even; that is legacy,
   not a precedent.
4. **Bad input is a 4xx, never a 500.** A handler raises `portal_api.errors.ClientError` with a stable
   `SCREAMING_SNAKE` code, and the response body is `{"error": CODE, "message": text}`. A 500 means a bug in our
   code, and the errors alarm pages someone for it.
5. **Python 3.12, standard library only.** Tests live in `<component>/tests/`, named
   `test_<component>_<module>.py`. A bug fix adds a test that fails before the fix.
6. **Merging does not deploy.** The release pipeline deploys `portal-api` to production and records the deployed
   revision; see `docs/runbook-portal-api.md`.

Local check before pushing: `pytest -q` from the repository root.
