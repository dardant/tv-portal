"""Subjects and bodies of customer emails."""

from __future__ import annotations


def shipped_subject(order: dict) -> str:
    """Subject line of the order-shipped email."""
    return f"Your order {order['id']} has shipped (tracking {order.get('tracking')})"


def shipped_body(order: dict) -> str:
    """Plain-text body of the order-shipped email."""
    lines = [f"Hi {order.get('customer_name', 'there')},", "", f"Order {order['id']} is on its way."]
    if order.get("tracking"):
        lines.append(f"Track it with {order.get('carrier', 'the carrier')}: {order['tracking']}")
    return "\n".join(lines)
