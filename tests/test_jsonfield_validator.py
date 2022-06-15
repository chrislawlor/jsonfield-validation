#!/usr/bin/env python

"""Tests for `jsonfield_validation` package."""

import pytest

from django.core.exceptions import ImproperlyConfigured, ValidationError
from jsonfield_validation import JsonSchemaValidator


def test_simple_validation(validator, valid_data):
    validator(valid_data)


def test_fails_with_invalid_data(validator):
    invalid_data = {"foo": "bar"}
    with pytest.raises(ValidationError):
        validator(invalid_data)


def test_improperly_configured_on_invalid_schema():
    bad_schema = {"type": "orange"}
    with pytest.raises(ImproperlyConfigured):
        JsonSchemaValidator(schema=bad_schema)


def test_nested_path_array_error_representation():

    schema = {
        "type": "object",
        "properties": {
            "points": {
                "type": "array",
                "items": {"$ref": "#/definitions/Point"},
            }
        },
        "required": ["points"],
        "definitions": {
            "Point": {
                "type": "object",
                "properties": {
                    "x": {"type": "integer"},
                    "y": {"type": "integer"},
                },
                "required": ["x", "y"],
            }
        },
    }
    # Second element is invalid type
    data = {"points": [{"x": 1, "y": 1}, "origin"]}
    validator = JsonSchemaValidator(schema=schema)

    try:
        validator(data)
    except ValidationError as ve:
        assert hasattr(ve, "error_dict")
        # Errors in array items are shown using index syntax
        assert "points.[1]" in ve.error_dict
        # Error list entries contain the path to the invalid value
        assert "points.[1]" in ve.error_list[0].message
