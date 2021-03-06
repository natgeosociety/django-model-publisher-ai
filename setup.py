#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


def get_readme():
    """Return the README file contents. Supports text,rst, and markdown"""
    for name in ('README', 'README.rst', 'README.md'):
        if os.path.exists(name):
            return read_file(name)
    return ''


setup(
    name='django-model-publisher-ai',
    version=__import__('publisher').get_version().replace(' ', '-'),
    description="""Handy mixin/abstract class for providing a "publisher workflow" to arbitrary Django models.""",
    long_description=get_readme(),
    author='Rich Temple',
    author_email='rtemple@celerity.com',
    url='https://github.com/natgeosociety/django-model-publisher-ai',
    packages=find_packages(exclude=['example*', ]),
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
    ],
)
