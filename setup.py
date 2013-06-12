#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='django-deferred-filelogger',
    version='0.1',
    description="A logging handler for Django that defers evaluation of the filepath",
    long_description=open('README.rst').read(),
    license=open('LICENSE').read(),
    url='https://github.com/codeinthehole/django-deferred-filelogger',
    author="David Winterbottom",
    author_email="david.winterbottom@gmail.com",
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=['django']
)
