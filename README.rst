============
Django-Geodz
============

django-geodz is a simple django app that provides out of the box algerian province and municipality
models and their respective data fixtures

you can use it for your own algeria-related projects

Quick start
-----------

1. Add "geodz" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'geodz',
    )

2. Run `python manage.py migrate` to create/migrate the models and data fixtures.