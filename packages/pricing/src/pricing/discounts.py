"""Coupon codes and what they are worth."""

from __future__ import annotations

#: Active coupons and their percentage off. Codes are case-insensitive.
COUPONS: dict[str, int] = {"WELCOME10": 10, "SPRING25": 25, "STAFF40": 40}


def coupon_percent(code: str) -> int:
    """The percentage a coupon takes off."""
    return COUPONS[code.strip().upper()]
