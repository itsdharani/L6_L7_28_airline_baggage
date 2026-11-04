
import pytest
from airline_baggage import baggage_fee, carry_on_ok, check_in_status


def test_baggage_fee_invalid_inputs():
    with pytest.raises(ValueError):
        baggage_fee("first", 20, "domestic", False)

    with pytest.raises(ValueError):
        baggage_fee("economy", -5, "domestic", False)


def test_baggage_fee_within_allowance():
    assert baggage_fee("economy", 20, "domestic", True) == 0


def test_baggage_fee_domestic():
    assert baggage_fee("economy", 25, "domestic", False) == 200


def test_baggage_fee_international_excess():
    assert baggage_fee("economy", 40, "international", False) == 2500


def test_baggage_fee_business_member():
    assert baggage_fee("business", 50, "international", True) == 450


def test_carry_on_cases():
    assert carry_on_ok(5, 2, True) is True
    assert carry_on_ok(8, 1, False) is False
    assert carry_on_ok(5, 1, False) is True
    assert carry_on_ok(5, 2, False) is False


def test_check_in_status():
    assert check_in_status(60, True, False) == "open"
    assert check_in_status(95, False, True) == "late"
    assert check_in_status(80, False, True) == "closed"

