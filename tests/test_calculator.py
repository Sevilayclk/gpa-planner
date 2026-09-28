from decimal import Decimal

import pytest

from gpa_planner.calculator import Course, calculate_gpa, letter_to_coefficient


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
# ---------- GPA calculation ----------

# REQ-03: GPA = sum(ECTS x coefficient) / sum(ECTS)
def test_gpa_single_course():
    assert calculate_gpa([Course("Math", 5, "AA")]) == Decimal("4.000")


def test_gpa_multiple_courses():
    courses = [Course("Math", 6, "AA"), Course("Physics", 4, "CC")]
    # (6*4.00 + 4*2.00) / 10 = 32 / 10 = 3.200
    assert calculate_gpa(courses) == Decimal("3.200")


# Boundary values: lowest and highest possible GPA
def test_gpa_all_ff_is_zero():
    assert calculate_gpa([Course("A", 5, "FF"), Course("B", 3, "FF")]) == Decimal("0.000")


def test_gpa_all_aa_is_four():
    assert calculate_gpa([Course("A", 5, "AA"), Course("B", 3, "AA")]) == Decimal("4.000")


# REQ-04: Rounded to 3 decimals with ROUND_HALF_UP
def test_gpa_rounds_half_up():
    courses = [Course("A", 7, "BB"), Course("B", 1, "BA")]
    # (7*3.00 + 1*3.50) / 8 = 24.5 / 8 = 3.0625 -> 3.063 (not 3.062!)
    assert calculate_gpa(courses) == Decimal("3.063")


def test_gpa_repeating_decimal():
    courses = [Course("A", 1, "AA"), Course("B", 1, "FF"), Course("C", 1, "FF")]
    # 4 / 3 = 1.3333... -> 1.333
    assert calculate_gpa(courses) == Decimal("1.333")


# REQ-05: ECTS must be a positive integer
@pytest.mark.parametrize("bad_ects", [0, -5, 2.5, "5", True])
def test_gpa_invalid_ects_raises(bad_ects):
    with pytest.raises(ValueError):
        calculate_gpa([Course("Math", bad_ects, "AA")])


# REQ-07: Empty course list raises an error
def test_gpa_empty_list_raises():
    with pytest.raises(ValueError):
        calculate_gpa([])