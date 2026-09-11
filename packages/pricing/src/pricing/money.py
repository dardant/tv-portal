"""Money arithmetic for quotes.

Legacy: amounts are floats. CONTRIBUTING.md rule 3 says new money code uses ``decimal.Decimal`` and rounds half
up to the cent; this module predates the rule.
"""

from __future__ import annotations


def line_total(unit_price: float, quantity: int) -> float:
    """``unit_price`` times ``quantity``, rounded to the cent."""
    if quantity < 1:
        raise ValueError("quantity must be at least 1")
    return round(unit_price * quantity, 2)


def apply_discount(amount: float, percent: float) -> float:
    """``amount`` reduced by ``percent`` per cent, rounded to the cent."""
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return round(amount * (1 - percent / 100), 2)
