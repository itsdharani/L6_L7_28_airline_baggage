
import pytest
from airline_baggage import baggage_fee, carry_on_ok, check_in_status


# Baggage fee tests

def test_invalid_cabin():
    with pytest.raises(ValueError):
        baggage_fee("first", 20, "domestic", False)


def test_invalid_weight():
    with pytest.raises(ValueError):
        baggage_fee("economy", -1, "domestic", False)


def test_membership_allowance():
    assert baggage_fee("economy", 30, "domestic", True) == 100
    assert baggage_fee("business", 50, "domestic", True) == 200


def test_excess_within_and_above_20():
    assert baggage_fee("economy", 20, "domestic", False) == 100
    assert baggage_fee("economy", 40, "domestic", False) == 1000


def test_domestic_and_international_routes():
    assert baggage_fee("economy", 25, "domestic", False) == 200
    assert baggage_fee("economy", 25, "international", False) == 450


def test_large_international_excess():
    assert baggage_fee("economy", 40, "international", False) == 2500


# Carry-on tests

def test_infant_carry_on():
    assert carry_on_ok(10, 2, True) is True
    assert carry_on_ok(10, 3, True) is False


def test_non_infant_weight_limit():
    assert carry_on_ok(8, 1, False) is False
    assert carry_on_ok(7, 1, False) is True


def test_non_infant_item_limit():
    assert carry_on_ok(5, 1, False) is True
    assert carry_on_ok(5, 2, False) is False


# Check-in status tests

@pytest.mark.parametrize(
    "minutes, baggage, international, expected",
    [
        (60, True, False, "open"),
        (50, True, False, "late"),
        (44, True, False, "closed"),

        (45, False, False, "open"),
        (35, False, False, "late"),
        (29, False, False, "closed"),

        (120, True, True, "open"),
        (110, True, True, "late"),
        (104, True, True, "closed"),

        (105, False, True, "open"),
        (95, False, True, "late"),
        (89, False, True, "closed"),
    ]
)
def test_check_in_status(minutes, baggage, international, expected):
    assert check_in_status(
        minutes, baggage, international
    ) == expected

