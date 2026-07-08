# FakeRestAPI API Testing with Pytest

A simple API automation testing project built with **Python**, **pytest**, and **requests** to validate CRUD operations on the FakeRestAPI service. This project demonstrates API testing fundamentals, including request validation, response verification, and test organization using pytest.

## Tech Stack

* Python
* pytest
* requests

## Project Structure

```text
.
├── reports/
│   └── report.html
├── screenshots/
│   ├── Test CLI report.png
│   └── Test HTML report.png
├── tests/
│   ├── test_activities.py
│   ├── test_authors.py
│   ├── test_books.py
│   ├── test_coverPhotos.py
│   └── test_users.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Test Coverage

The project covers CRUD testing for the following API resources:

| Resource   | GET | POST | PUT | DELETE |
| ---------- | :-: | :--: | :-: | :----: |
| Books      |  ✅  |   ✅  |  ✅  |    ✅   |
| Authors    |  ✅  |   ✅  |  ✅  |    ✅   |
| Activities |  ✅  |   ✅  |  ✅  |    ✅   |
| CoverPhotos|  ✅  |   ✅  |  ✅  |    ✅   |
| Users      |  ✅  |   ✅  |  ✅  |    ✅   |

## How to Run

1. Clone the repository.
2. Create and activate a virtual environment.

```bash
python -m venv .venv
```

**Windows (PowerShell)**

```bash
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies.

```bash
pip install -r requirements.txt
```

4. Run all tests.

```bash
pytest -v
```

## Project Highlights

* API automation using pytest
* CRUD endpoint validation
* Response status code verification
* Response body validation
* Clean and organized test structure

## Notes

This project uses FakeRestAPI, which is a mock API. Some endpoints do not perform full server-side validation, so certain negative scenarios (such as updating or deleting non-existing resources) may return successful responses instead of the status codes typically expected from a production API.
