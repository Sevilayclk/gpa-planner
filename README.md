\# GPA Planner



!\[Tests](https://github.com/Sevilayclk/gpa-planner/actions/workflows/tests.yml/badge.svg)



A GPA calculator based on the ECTS (AKTS) credit system, built with Python

using Test-Driven Development (TDD).



\## Features



\- Letter grade to coefficient conversion (AA = 4.00 ... FF = 0.00)

\- ECTS-weighted GPA calculation

\- Rounding to 3 decimal places with ROUND\_HALF\_UP

\- Input validation (invalid ECTS, unknown letter grades, empty course list)



See \[docs/requirements.md](docs/requirements.md) for the full requirements.



\## Setup



```bash

git clone https://github.com/Sevilayclk/gpa-planner.git

cd gpa-planner

python -m venv .venv

.venv\\Scripts\\activate        # Windows

source .venv/bin/activate     # macOS / Linux

pip install -r requirements.txt

```



\## Running Tests



```bash

pytest -v

pytest --cov=gpa\_planner --cov-branch --cov-report=term-missing

```



\## Testing Approach



\- \*\*TDD:\*\* tests are written before the code (red -> green -> refactor)

\- \*\*Traceability:\*\* every test is linked to a requirement ID (REQ-xx)

\- \*\*Test design techniques:\*\* boundary value analysis, equivalence partitioning, negative testing

\- \*\*Coverage:\*\* 100% statement and branch coverage

\- \*\*CI:\*\* GitHub Actions runs all tests on Python 3.12 and 3.13 on every push



\## Roadmap



\- \[x] Core GPA calculation with tests

\- \[x] Continuous Integration

\- \[ ] REST API (FastAPI) with API tests

\- \[ ] Web interface with end-to-end tests (Playwright)

\- \[ ] Target GPA planner



\## License



MIT

