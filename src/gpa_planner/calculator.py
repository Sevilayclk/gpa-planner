from decimal import Decimal

GRADE_TABLE = {
    "AA": Decimal("4.00"),
    "BA": Decimal("3.50"),
    "BB": Decimal("3.00"),
    "CB": Decimal("2.50"),
    "CC": Decimal("2.00"),
    "DC": Decimal("1.50"),
    "DD": Decimal("1.00"),
    "FD": Decimal("0.50"),
    "FF": Decimal("0.00"),
}


def letter_to_coefficient(letter: str) -> Decimal:
    """Convert a letter grade to its coefficient (REQ-02, REQ-06, REQ-08)."""
    key = letter.upper()
    if key not in GRADE_TABLE:
        raise ValueError(f"Unknown letter grade: {letter!r}")
    return GRADE_TABLE[key]