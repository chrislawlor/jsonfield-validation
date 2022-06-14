from django.db import models

try:
    from django.db.models import JSONField
except ImportError:
    # For Django < 3.1
    from jsonfield import JSONField

from jsonfield_validation import JsonSchemaValidator


SCHEMA = {
    "type": "object",
    "properties": {
        "first_name": {"type": "string"},
        "last_name": {"type": "string"},
        "birthday": {"type": "string", "format": "date"},
        "address": {
            "type": "object",
            "properties": {
                "street_address": {"type": "string"},
                "city": {"type": "string"},
                "state": {"type": "string"},
                "country": {"type": "string"},
            },
        },
    },
    "additionalProperties": False,
}


class MyModel(models.Model):
    data = JSONField(validators=[JsonSchemaValidator(SCHEMA)])


class ShortListModel(models.Model):
    data = JSONField(
        validators=[
            JsonSchemaValidator(
                {"type": "array", "maxItems": 2, "items": {"type": "number"}}
            )
        ]
    )
