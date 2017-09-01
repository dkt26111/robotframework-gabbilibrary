#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from os.path import join, dirname
execfile(join(dirname(__file__), 'src', 'GabbiLibrary', 'version.py'))
long_description = open(join(dirname(__file__), 'README.md',)).read()

CLASSIFIERS = """
Programming Language :: Python
Topic :: Software Development :: Testing
"""[1:-1]

setup(
    name='robotframework-gabbilibrary',
    version=VERSION,
    description='Robot framework test library for Gabbi tests ',
    long_description=long_description,
    author='Duc Truong',
    author_email='dkt26111@gmail.com',
    url='https://github.com/dkt26111/robotframework-gabbilibrary',
    license='Apache License 2.0',
    packages=['GabbiLibrary'],
    package_dir={'': 'src'},
    install_requires=['robotframework', 'gabbi'],
    zip_safe=False,
    keywords='robotframework gabbi http testing',
    classifiers=CLASSIFIERS.splitlines()
)
