#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = ["Django", "jsonschema"]

test_requirements = [
    "pytest>=3",
]

setup(
    author="Chris Lawlor",
    author_email="lawlor.chris@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
    ],
    description="Validator class for Django model JSON fields.",
    install_requires=requirements,
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="jsonfield_validation",
    name="jsonfield_validation",
    packages=find_packages(include=["jsonfield_validation", "jsonfield_validation.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/chrislawlor/jsonfield-validation",
    version="0.3.0",
    zip_safe=False,
)
