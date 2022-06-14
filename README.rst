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
                JsonSchemaValidator({"maxItems": 2)
            ]
        )

Credits
-------

This package was created with Cookiecutter_ and the `pymetrics/cookiecutter-python-library`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/pymetrics/cookiecutter-python-library
