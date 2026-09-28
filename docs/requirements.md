\# GPA Planner – Requirements (MVP)



| ID | Requirement |

|---|---|

| REQ-01 | User enters each course with name, ECTS (AKTS) credits and letter grade |

| REQ-02 | Letter grades map to coefficients using the grade table below |

| REQ-03 | GPA = sum(ECTS × coefficient) / sum(ECTS) |

| REQ-04 | GPA is rounded to 3 decimal places using ROUND\_HALF\_UP |

| REQ-05 | ECTS must be a positive integer; otherwise an error is raised |

| REQ-06 | Unknown letter grades (e.g. "XY") raise an error |

| REQ-07 | An empty course list raises an error (no division by zero) |

| REQ-08 | Letter grades are case-insensitive ("aa" == "AA") |



\## Grade Table



| Letter | AA | BA | BB | CB | CC | DC | DD | FD | FF |

|---|---|---|---|---|---|---|---|---|---|

| Coefficient | 4.00 | 3.50 | 3.00 | 2.50 | 2.00 | 1.50 | 1.00 | 0.50 | 0.00 |

