import pytest

from portal_api.inventory import suggest_topup


def test_above_reorder_point_suggests_nothing():
    assert suggest_topup(11, 10, 50) == 0


def test_at_reorder_point_tops_up_to_target():
    assert suggest_topup(10, 10, 50) == 40


def test_below_reorder_point_tops_up_to_target():
    assert suggest_topup(5, 10, 50) == 45


def test_at_target_suggests_nothing():
    assert suggest_topup(50, 10, 50) == 0


def test_zero_quantity_tops_up_to_target():
    assert suggest_topup(0, 10, 50) == 50


def test_zero_reorder_point_and_target():
    assert suggest_topup(0, 0, 0) == 0


@pytest.mark.parametrize("quantity,reorder_point,target_level", [(-1, 10, 50), (5, -1, 50), (5, 10, -1)])
def test_negative_inputs_raise(quantity, reorder_point, target_level):
    with pytest.raises(ValueError):
        suggest_topup(quantity, reorder_point, target_level)


@pytest.mark.parametrize(
    "quantity,reorder_point,target_level", [(5.0, 10, 50), (5, "10", 50), (5, 10, None), (True, 10, 50)]
)
def test_non_int_inputs_raise(quantity, reorder_point, target_level):
    with pytest.raises(ValueError):
        suggest_topup(quantity, reorder_point, target_level)


def test_target_below_reorder_raises():
    with pytest.raises(ValueError):
        suggest_topup(5, 10, 9)


def test_target_equal_to_reorder_tops_up_difference():
    assert suggest_topup(5, 10, 10) == 5
    assert suggest_topup(10, 10, 10) == 0


def test_quantity_above_target_and_reorder_suggests_nothing():
    assert suggest_topup(60, 10, 50) == 0


@pytest.mark.parametrize(
    "quantity,reorder_point,target_level",
    [(True, 10, 50), (5, True, 50), (5, False, 50), (5, 10, True), (5, 10, False)],
)
def test_bool_inputs_raise_in_every_position(quantity, reorder_point, target_level):
    with pytest.raises(ValueError):
        suggest_topup(quantity, reorder_point, target_level)
