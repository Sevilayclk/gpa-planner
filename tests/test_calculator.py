from decimal import Decimal

import pytest

from gpa_planner.calculator import letter_to_coefficient


# REQ-02: Letter grades map to coefficients
@pytest.mark.parametrize( 
# @pytest.mark.parametrize → aynı testi 9 farklı veriyle çalıştırır. 9 ayrı 
# fonksiyon yazmak yerine tek fonksiyon = data-driven testing
    "letter, expected",
    [
        ("AA", Decimal("4.00")),
        ("BA", Decimal("3.50")),
        ("BB", Decimal("3.00")),
        ("CB", Decimal("2.50")),
        ("CC", Decimal("2.00")),
        ("DC", Decimal("1.50")),
        ("DD", Decimal("1.00")),
        ("FD", Decimal("0.50")),
        ("FF", Decimal("0.00")),
    ],
)
def test_letter_to_coefficient_valid(letter, expected):
    assert letter_to_coefficient(letter) == expected


# REQ-08: Letter grades are case-insensitive
def test_letter_to_coefficient_lowercase():
    assert letter_to_coefficient("ba") == Decimal("3.50")


# REQ-06: Unknown letter grades raise an error
def test_letter_to_coefficient_unknown_raises():
    with pytest.raises(ValueError):
        letter_to_coefficient("XY")