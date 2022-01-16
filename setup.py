#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

version = "1.0.1"

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()


def read(filename):
    with open(filename) as f:
        return f.read()


readme = read("README.rst")
history = read("HISTORY.rst").replace(".. :changelog:", "")
requirements = [
    "django>=2.2.13,<5.0",
    "wheel",
]
test_requirements = read("requirements-test.txt").splitlines()

setup(
    name="django-dedal",
    version=version,
    description="""Fast CRUD builder.""",
    long_description=readme + "\n\n" + history,
    author="Arkadiusz Adamski",
    author_email="arkadiusz.adamski@gmail.com",
    url="https://github.com/ar4s/django-dedal",
    packages=[
        "dedal",
    ],
    include_package_data=True,
    install_requires=requirements,
    tests_require=requirements + test_requirements,
    license="BSD",
    zip_safe=False,
    keywords="django-dedal",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
