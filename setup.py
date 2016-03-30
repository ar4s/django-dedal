#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

version = '1.0.1'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()


def read(filename):
    with open(filename) as f:
        return f.read()

readme = read('README.rst')
history = read('HISTORY.rst').replace('.. :changelog:', '')
requirements = [
    'django>=1.8',
    'django-bootstrap-form==3.2',
    'wheel==0.24.0',
]
test_requirements = read('requirements-test.txt').splitlines()

setup(
    name='django-dedal',
    version=version,
    description="""Fast CRUD builder.""",
    long_description=readme + '\n\n' + history,
    author='Arkadiusz Adamski',
    author_email='arkadiusz.adamski@gmail.com',
    url='https://github.com/ar4s/django-dedal',
    packages=[
        'dedal',
    ],
    include_package_data=True,
    install_requires=requirements,
    tests_require=requirements + test_requirements,
    license="BSD",
    zip_safe=False,
    keywords='django-dedal',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Framework :: Django :: 1.6',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
