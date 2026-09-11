from pricing import add_tax, rate_for


def test_rate_for_a_supported_region():
    assert rate_for("de") == 0.19


def test_add_tax_rounds_to_the_cent():
    assert add_tax(20.0, "DE") == 23.8
