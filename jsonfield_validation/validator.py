from collections import defaultdict
from typing import Any, Dict, Iterable, List, Optional

from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.utils.deconstruct import deconstructible
from jsonschema import SchemaError
from jsonschema import ValidationError as SchemaValidationError
from jsonschema.validators import validator_for

# NOTE: The deconstructible decorator allows Django to serialize the
# validator instance, this plus the __eq__ method prevent new migrations
# being created on every makemigrations run.
# See https://docs.djangoproject.com/en/4.0/topics/migrations/#adding-a-deconstruct-method  # noqa


@deconstructible
class JsonSchemaValidator:
    """
    Django model field validator for use with JSONField.

    Validates against a given JSON Schema.
    """

    nested_item_delimiter = "."

    def __init__(self, schema: Dict):
        self.validator = validator_for(schema)(schema)
        try:
            self.validator.check_schema(schema)
        except SchemaError as e:
            raise ImproperlyConfigured("Not a valid JSON schema") from e
        self.schema = schema

    def __call__(self, value):
        errors = self.check(value)
        if errors is not None:
            # Field.run_validators doesn't work with dict-based ValidationErrors,
            # so we set error_list as the list of errors, but also set
            # error_dict explicitly.
            # See https://code.djangoproject.com/ticket/29318
            ve = ValidationError(self._errordict_to_list(errors))
            ve.error_dict = errors
            raise ve

    def check(self, value) -> Optional[Dict]:
        """
        Check value against the schema without raising an exception.

        If there are errors, they are returned as a dictionary. If the
        value is a JSON object, errors are keyed by the path through to
        the errant attribute.
        """
        errors = []
        for error in sorted(self.validator.iter_errors(value), key=str):
            errors.append(error)
        if errors:
            return self._errors_to_dict(errors)
        return None

    @classmethod
    def _errors_to_dict(
        cls,
        error_list: Iterable[SchemaValidationError],
    ) -> Dict[str, List[str]]:
        """
        Convert a list of jsonschema ValidationError to a dictionary.

        For an object with nested values, dict keys will be flattened
        using the nested_item_delimiter. If an error is not related to
        an individual attribute, it will be listed under the key
        "__non_field_errors__".

        The value will be a list of errors pertaining to that key.
        """
        errors = defaultdict(list)
        for ve in error_list:
            key = cls.nested_item_delimiter.join(cls._stringify_path_elements(ve.path))
            key = key or "__non_field_errors__"
            errors[key].append(ve.message)
        return errors

    @classmethod
    def _errordict_to_list(cls, errordict: Dict[str, List[str]]) -> List[str]:
        """
        Flatten the error dict down to a list of strings by prepending
        each error value with the error key.
        """

        return [f"{k}: {v}" for k, v in errordict.items()]

    @classmethod
    def _stringify_path_elements(cls, path: Iterable[Any]) -> List[str]:
        elements = []
        for p in path:
            if isinstance(p, int):
                elements.append(f"[{p}]")
            else:
                elements.append(str(p))
        return elements

    def __eq__(self, other):
        return isinstance(other, JsonSchemaValidator) and self.schema == other.schema
