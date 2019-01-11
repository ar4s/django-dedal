=============================
django-dedal
=============================

.. image:: https://img.shields.io/pypi/v/django-dedal.svg?style=flat-square
    :target: https://pypi.python.org/pypi/django-dedal

.. image:: https://img.shields.io/pypi/pyversions/django-dedal.svg?style=flat-square
    :target: https://pypi.python.org/pypi/django-dedal

.. image:: https://img.shields.io/travis/ar4s/django-dedal.svg?style=flat-square
    :target: https://travis-ci.org/ar4s/django-dedal

.. image:: https://img.shields.io/coveralls/ar4s/django-dedal.svg?style=flat-square
    :target: https://coveralls.io/r/ar4s/django-dedal?branch=master

Fast CRUD builder.

Documentation
-------------

The full documentation is at https://django-dedal.readthedocs.org.

Demo
----

Example project is available on http://django-dedal.herokuapp.com/.

Quickstart
----------

Install django-dedal::

    pip install django-dedal

Then use it in a Django project simple add ``dedal`` and ``bootstrapform`` (if you want use bootstrap) to ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        ...
        'dedal',
        'bootstrapform',
    )

After this decorate your model by ``@crud``::

    from django.db import models

    from dedal.decorators import crud


    @crud
    class Post(models.Model):
        title = models.CharField(max_length=50)
        body = models.TextField()
        comments = models.ManyToManyField('Comment', blank=True)

        def __str__(self):
            return '{}'.format(self.title)

That's all!

TODO
----
* select related
