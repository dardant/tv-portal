from portal_api.handlers import health, quote


def test_health_reports_the_version():
    status, body = health()
    assert status == 200
    assert body["ok"] is True


def test_quote_prices_a_basket_with_tax():
    status, body = quote({"items": [{"sku": "A", "unit_price": 10.0, "quantity": 2}], "region": "DE"})
    assert status == 200
    assert body["subtotal"] == 20.0
    assert body["total"] == 23.8


def test_quote_applies_a_coupon_before_tax():
    status, body = quote(
        {"items": [{"sku": "A", "unit_price": 100.0, "quantity": 1}], "region": "US-NY", "coupon": "WELCOME10"}
    )
    assert status == 200
    assert body["discount_percent"] == 10
    assert body["total"] == 93.6


def test_a_quote_without_items_is_a_client_error():
    status, body = quote({"items": [], "region": "DE"})
    assert status == 400
    assert body["error"] == "ITEMS_REQUIRED"
