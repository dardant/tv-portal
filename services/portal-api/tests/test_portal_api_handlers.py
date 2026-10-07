from portal_api.handlers import health, quote, suggest


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


def test_suggest_tops_up_when_at_or_below_reorder():
    status, body = suggest({"quantity": 5, "reorder_point": 10, "target_level": 50})
    assert status == 200
    assert body["suggested_quantity"] == 45


def test_suggest_returns_zero_above_reorder():
    status, body = suggest({"quantity": 11, "reorder_point": 10, "target_level": 50})
    assert status == 200
    assert body["suggested_quantity"] == 0


def test_suggest_missing_field_is_a_client_error():
    status, body = suggest({"quantity": 5, "reorder_point": 10})
    assert status == 400
    assert body["error"] == "MISSING_FIELD"


def test_suggest_invalid_input_is_a_client_error_not_a_500():
    for bad in [
        {"quantity": -1, "reorder_point": 10, "target_level": 50},
        {"quantity": 5.0, "reorder_point": 10, "target_level": 50},
        {"quantity": 5, "reorder_point": 10, "target_level": 9},
    ]:
        status, body = suggest(bad)
        assert status == 400
        assert body["error"] == "INVALID_TOPUP_INPUT"


def test_suggest_success_echoes_inputs_with_suggestion():
    status, body = suggest({"quantity": 5, "reorder_point": 10, "target_level": 50})
    assert status == 200
    assert body == {
        "quantity": 5,
        "reorder_point": 10,
        "target_level": 50,
        "suggested_quantity": 45,
    }


def test_suggest_quantity_above_target_suggests_nothing():
    status, body = suggest({"quantity": 60, "reorder_point": 10, "target_level": 50})
    assert status == 200
    assert body["suggested_quantity"] == 0


def test_suggest_bool_and_string_inputs_are_client_errors_not_500():
    for bad in [
        {"quantity": True, "reorder_point": 10, "target_level": 50},
        {"quantity": 5, "reorder_point": 10, "target_level": "50"},
        {"quantity": 5, "reorder_point": 10, "target_level": 9},
    ]:
        status, body = suggest(bad)
        assert status == 400
        assert body["error"] == "INVALID_TOPUP_INPUT"
        assert body["message"]
        assert status != 500
