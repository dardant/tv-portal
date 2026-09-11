"""Turn account events into customer emails."""

from __future__ import annotations


def build_digest(events: list[dict]) -> list[dict]:
    """One email per event, addressed to the event's customer."""
    return [
        {"to": event["customer_email"], "subject": f"Account update: {event['kind']}", "items": [event]}
        for event in events
    ]
