"""Sales tax by region."""

from __future__ import annotations

#: Rates by region code. A region missing from this table is not supported yet.
RATES: dict[str, float] = {"US-CA": 0.0725, "US-NY": 0.04, "US-WA": 0.065, "DE": 0.19, "GB": 0.20}


def rate_for(region: str) -> float:
    """The sales-tax rate for ``region``."""
    return RATES[region.upper()]


def add_tax(amount: float, region: str) -> float:
    """``amount`` with ``region``'s sales tax added, rounded to the cent."""
    return round(amount * (1 + rate_for(region)), 2)
