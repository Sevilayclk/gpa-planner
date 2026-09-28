from dataclasses import dataclass
from decimal import ROUND_HALF_UP, Decimal

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
@dataclass
class Course:
    name: str
    ects: int
    letter: str


def calculate_gpa(courses: list[Course]) -> Decimal:
    """Calculate ECTS-weighted GPA (REQ-03, REQ-04, REQ-05, REQ-07)."""
    if not courses:
        raise ValueError("Course list is empty")

    total_points = Decimal("0")
    total_ects = 0
    for course in courses:
        # bool is a subclass of int in Python, so exclude it explicitly
        if isinstance(course.ects, bool) or not isinstance(course.ects, int) or course.ects <= 0:
            raise ValueError(f"Invalid ECTS for {course.name!r}: {course.ects!r}")
        total_points += course.ects * letter_to_coefficient(course.letter)
        total_ects += course.ects

    gpa = total_points / total_ects
    return gpa.quantize(Decimal("0.001"), rounding=ROUND_HALF_UP)