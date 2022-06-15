.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/chrislawlor/jsonfield-validation/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

Django JSON Schema Field Validator could always use more documentation, whether as part of the
official Django JSON Schema Field Validator docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/chrislawlor/jsonfield_validation/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `jsonfield_validation` for local development.

1. Fork the `jsonfield_validation` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/jsonfield_validation.git

3. If you're using asdf_, run ``asdf install`` to install the Pythons listed in ``.tool-versions``.
   Add the asdf-python_ plugin if you don't have it already.

4. Install your local copy into a virtualenv. Assuming you have tox_ installed, this is how you set up your fork for local development::

    $ make develop

   This will create a virtual environment in the ``.env`` directory, enable it, and
   install all project and development dependencies.

   Alternately, with virtualenvwrapper_:

    $ mkvirtualenv jsonfield_validation
    $ cd jsonfield_validation/
    $ python setup.py develop
    $ python -m pip install -r requirements_dev.txt


.. _asdf: https://asdf-vm.com/
.. _asdf-python: https://github.com/danhper/asdf-python
.. _tox: https://tox.wiki/en/latest/index.html
.. _virtualenvwrapper: https://virtualenvwrapper.readthedocs.io/en/latest/


4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the
   tests, including testing other Python versions with tox::

    $ make lint
    $ make test
    $ tox

   To get flake8 and tox, just pip install them into your virtualenv. Check ``tox.ini``
   for the Python versions you'll need available. If you're using asdf_, simply
   run ``asdf install``.

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 3.6, 3.7, 3.8, and 3.9. Check
   https://travis-ci.com/chrislawlor/jsonfield_validation/pull_requests
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests::

$ pytest tests.test_jsonfield_validation


Publishing
----------

A reminder for the maintainers on how to publish.
Make sure all your changes are committed (including an entry in HISTORY.rst).
Then run::

$ bump2version patch # possible: major / minor / patch
$ git push
$ git push --tags

Travis will then deploy to PyPI if tests pass.
