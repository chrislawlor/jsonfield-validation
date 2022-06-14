==================================
Django JSON Schema Field Validator
==================================

.. image:: https://app.travis-ci.com/chrislawlor/jsonfield-validation.svg?branch=master
    :target: https://app.travis-ci.com/chrislawlor/jsonfield-validation

.. image:: https://readthedocs.org/projects/jsonfield-validation/badge/?version=latest
    :target: https://jsonfield-validation.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

JSON Schema validation for Django JSONField.


Quickstart
----------

Installation
++++++++++++

.. code:: bash

    pip install jsonfield-validation

Usage
+++++

.. code:: python

    from jsonfield_validation import JsonSchemaValidator


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


Further documentation is gratiously hosted by `Read the Docs`_

Credits
-------

This package was created with Cookiecutter_ and the `pymetrics/cookiecutter-python-library`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`pymetrics/cookiecutter-python-library`: https://github.com/pymetrics/cookiecutter-python-library
.. _`Read the Docs`: https://jsonfield-validation.readthedocs.io