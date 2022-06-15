=====
Usage
=====

Validating JSONField
--------------------

Create a validator by passing a valid JSON schema to
``JsonSchemaValidator``:

.. code:: python

    from jsonfield_validation import JsonSchemaValidator

    max2 = JsonSchemaValidator({"maxItems": 2})

    class MyModel(models.Model):
        items = models.JSONField(validators=[max2])


As with any Django model validators, be sure to call ``clean_fields``
if necessary:

.. code:: python

    instance = MyModel(items=[1, 2, 3])

    instance.clean_fields()

    django.core.exceptions.ValidationError: {'items': ["[1, 2, 3] is too long"]}



JSONField support
+++++++++++++++++

``JsonSchemaValidator`` is tested against the JSONField
implementation included in Django > 3.1, and
against django-jsonfield_ for prior versions of Django.

.. _django-jsonfield: https://pypi.org/project/django-jsonfield/


Generating JSON schemas with Pydantic
-------------------------------------

Pydantic_ is a great fit for Django JSON Field Validator:

.. code:: python

    from django.db import models
    from pydantic import BaseModel


    class Point(BaseModel):
        x: int
        y: int


    class Points(BaseModel):
        __root__: List[Point]


    class Shape(models.Model):
        points: models.JSONField(
            validators=[JsonSchemaValidator(schema=Points.schema())]
        )

.. _Pydantic: https://pydantic-docs.helpmanual.io/


Testing a schema against existing data
--------------------------------------

If you're adding schema validation to a model
with existing records, you may wish to verify
that the existing data will match the proposed schema.

The ``JsonSchemaValidator`` provides a ``check`` method,
which will run schema validation without raising an exception.
This is ideal for validating many objects without the overhead
of exception handling.

The ``check`` method will return an error dict if validation
fails, and ``None`` if it succeeds. Errors are keyed by
the flattened path to the errant value. Nested keys are
concatenated with a ``.`` by default. If the error occurs
in a list, the errant item's position is noted with
square brackets, using standard 0-based indexing.


As an example, here's a nested object containing
a list that is meant to be all numbers, but a string
snuck in:

.. code:: python

    data = {
        "students": {
            "Alice": {
                "scores": [85, 92, "A"]
            {
        }
    }

The key in the error dict for this would be ``"students.Alice.scores.[2]"``:

.. code:: python

    validator = JsonSchemaValidator(...)

    validator.check(data)

    {"students.Alice.scores.[2]": "'A' is not a number"}



A simple check against
all records could then be performed like:

.. code:: python

    validator = JsonSchemaValidator({"maxItems": 2})

    if any(validator.check(obj.json_field) for obj in MyModel.objects.iterator()):
        print("Validation failed")


Of course, if validation does fail, you'll probably want to know
which object failed, and why. A more robust example:

.. code:: python

    validator = JsonSchemaValidator({"maxItems": 2})
    error_map = {}
    for obj in MyModel.objects.iterator():
        errors = validator.check(obj)
        if errors:
            error_map[obj.id] = errors
