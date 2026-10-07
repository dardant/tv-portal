# Changelog: portal-api

Every change to this component adds a line under **Unreleased** (CONTRIBUTING.md, rule 1). The version in
`src/portal_api/handlers.py` is bumped by the release pipeline, not by a change.

## Unreleased

### Added
- Top-up suggestions (Story INV-302): `portal_api.inventory.suggest_topup` plus `POST /suggest` handler returning `suggested_quantity` with 4xx `MISSING_FIELD` / `INVALID_TOPUP_INPUT` on bad input.

## 1.4.2 - 2026-09-11

### Fixed
- `/quote` rounds the subtotal once instead of per line.

## 1.4.0 - 2026-08-30

### Added
- Coupons on `/quote`.
