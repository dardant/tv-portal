import pytest
from pricing import apply_discount, line_total


def test_line_total_multiplies_and_rounds_to_the_cent():
    assert line_total(19.99, 3) == 59.97


def test_line_total_rejects_a_zero_quantity():
    with pytest.raises(ValueError):
        line_total(1.0, 0)


def test_apply_discount_takes_the_percentage_off():
    assert apply_discount(100.0, 10) == 90.0


def test_apply_discount_rejects_more_than_everything():
    with pytest.raises(ValueError):
        apply_discount(100.0, 101)
