============
django-geodz
============

.. image:: https://badge.fury.io/py/django-geodz.svg
    :target: http://badge.fury.io/py/django-geodz

.. image:: https://pypip.in/download/django-geodz/badge.png
    :target: https://pypi.python.org/pypi/django-geodz/
    :alt: Downloads

.. image:: https://pypip.in/license/django-geodz/badge.png
    :target: https://pypi.python.org/pypi/django-geodz/
    :alt: License

django-geodz is a simple django app that provides out of the box algerian province and municipality
models and their respective data fixtures.

you can use it for your own algeria-related projects

also included:

- admin support
- fr locale translation
- support for both django 1.7 migrations, aswell as south migrations (requires atleast south 1.0)

Requirements
------------
- django-geoposition

Quick start
-----------

1. Add "geodz" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'geoposition',
        'geodz',
    )

2. Run `python manage.py migrate` to create/migrate the models and load the data fixtures.
3. use the provided models::

    from geodz.models import Province, Municipality

3. Profit !!!!


Changelog
---------

April 25th, 2015
----------------
- new `Region` model
- provinces now have a one-to many foreign key to regions
- initial data fixture updated
- south migrations deprecated / no longer supported / kept as is