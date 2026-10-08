# Changelog: portal-api

Every change to this component adds a line under **Unreleased** (CONTRIBUTING.md, rule 1). The version in
`src/portal_api/handlers.py` is bumped by the release pipeline, not by a change.

## Unreleased

### Added
- `POST /quote` accepts an optional `currency` (default `"USD"`); only `USD` and `EUR`
  (case-insensitive) are accepted and any other currency is a `400 UNSUPPORTED_CURRENCY` error.

## 1.4.2 - 2026-09-11

### Fixed
- `/quote` rounds the subtotal once instead of per line.

## 1.4.0 - 2026-08-30

### Added
- Coupons on `/quote`.
