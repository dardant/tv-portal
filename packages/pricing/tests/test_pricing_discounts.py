from pricing import coupon_percent


def test_coupon_codes_are_case_insensitive():
    assert coupon_percent("welcome10") == 10


def test_surrounding_whitespace_is_ignored():
    assert coupon_percent("  SPRING25 ") == 25
