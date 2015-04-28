import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-geodz',
    version='0.5.1',
    packages=['geodz'],
    include_package_data=True,
    license='BSD License',
    description='A simple django app that provides out of the box algerian province and municipality models and their respective data fixtures.',
    long_description=README,
    url='https://www.github.com/redouane/django-geodz',
    author='Redouane Zait',
    author_email='redouanezait@gmail.com',
    install_requires=['Django', 'django-geoposition'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ],
)
