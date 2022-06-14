==================================
Django JSON Schema Field Validator
==================================


JSON Schema validation for Django JSONField.


Quickstart
----------

Installation
++++++++++++

.. code:: bash

    pip install jsonfield-validator

Usage
+++++

.. code:: python

    from jsonfield_validator import JsonSchemaValidator


    class MyModel(models.Model):
        items = models.JSONField(
            validators=[
                JsonSchemaValidator({"maxItems": 2})
            ]
        )


Like any Django model field validator, validation happens
when ``clean_fields()`` is called on a model instance:


.. code:: python

    >>> instance = MyModel(items=[1, 2, 3])
    >>> instance.clean_fields()

    django.core.exceptions.ValidationError: {'items': ["[1, 2, 3] is too long"]}



Credits
-------

This package was created with Cookiecutter_ and the `pymetrics/cookiecutter-python-library`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`pymetrics/cookiecutter-python-library`: https://github.com/pymetrics/cookiecutter-python-library
