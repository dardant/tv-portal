"""Inventory reorder suggestions (Story INV-302).

Standard ``(s, S)`` policy: when on-hand ``quantity`` is at or below
``reorder_point`` (``s``), suggest a top-up to ``target_level`` (``S``);
otherwise suggest nothing. Suggestions are non-negative integers; money
rules (FIN-7) do not apply.
"""

from __future__ import annotations

__all__ = ["suggest_topup"]


def suggest_topup(quantity: int, reorder_point: int, target_level: int) -> int:
    """Suggest a top-up quantity to reach ``target_level``.

    Returns ``max(target_level - quantity, 0)`` when ``quantity`` is at or
    below ``reorder_point``, else ``0``. Never returns a negative value.

    Raises:
        ValueError: If any argument is not a non-negative ``int`` (bools
            rejected) or if ``target_level`` is below ``reorder_point``.
    """
    for name, value in (
        ("quantity", quantity),
        ("reorder_point", reorder_point),
        ("target_level", target_level),
    ):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"{name} must be a non-negative integer")
        if value < 0:
            raise ValueError(f"{name} must be a non-negative integer")
    if target_level < reorder_point:
        raise ValueError("target_level must be at least reorder_point")
    if quantity <= reorder_point:
        return max(target_level - quantity, 0)
    return 0
