import pytest

from jsonfield_validation import JsonSchemaValidator
from .app.models import SCHEMA


@pytest.fixture
def schema():
    return SCHEMA


@pytest.fixture
def valid_data():
    return {
        "first_name": "George",
        "last_name": "Washington",
        "birthday": "1732-02-22",
        "address": {
            "street_address": "3200 Mount Vernon Memorial Highway",
            "city": "Mount Vernon",
            "state": "Virginia",
            "country": "United States",
        },
    }


@pytest.fixture
def validator(schema) -> JsonSchemaValidator:
    return JsonSchemaValidator(schema=schema)
