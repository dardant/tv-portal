"""Request handlers for the portal API.

Transport-free on purpose: a handler takes the decoded JSON request and returns ``(status, body)``. The HTTP
adapter that serves them in production is not part of this repository.
"""

from __future__ import annotations

from pricing import add_tax, apply_discount, coupon_percent, line_total

from portal_api.errors import ClientError

VERSION = "1.4.2"


def health() -> tuple[int, dict]:
    """``GET /health``."""
    return 200, {"ok": True, "version": VERSION}


def quote(request: dict) -> tuple[int, dict]:
    """``POST /quote``: price a basket.

    Request: ``{"items": [{"sku", "unit_price", "quantity"}], "region": "US-CA", "coupon": "WELCOME10"}``, where
    ``coupon`` is optional. Response: ``{"subtotal", "discount_percent", "total"}``.
    """
    try:
        return 200, _quote(request)
    except ClientError as exc:
        return exc.status, {"error": exc.code, "message": str(exc)}
    except Exception:
        # The handler boundary: anything that is not a ClientError is our bug, not the caller's.
        return 500, {"error": "INTERNAL", "message": "internal error"}


def _quote(request: dict) -> dict:
    items = request.get("items") or []
    if not items:
        raise ClientError("ITEMS_REQUIRED", "a quote needs at least one item")
    subtotal = round(sum(line_total(item["unit_price"], item["quantity"]) for item in items), 2)
    percent = coupon_percent(request["coupon"]) if request.get("coupon") else 0
    discounted = apply_discount(subtotal, percent)
    total = add_tax(discounted, request.get("region", "US-CA"))
    return {"subtotal": subtotal, "discount_percent": percent, "total": total}
