=====
Usage
=====

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
