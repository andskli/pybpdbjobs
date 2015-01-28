#!/usr/bin/env python

import pybpdbjobs

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst', 'r') as f:
    readme = f.read()

packages = [
    'pybpdbjobs',
]

requires = []

setup(
    name='pybpdbjobs',
    version=pybpdbjobs.__version__,
    description='Library for parsing output from bpdbjbos',
    long_description=readme,
    author=pybpdbjobs.__author__,
    author_email='andreas@superblock.se',
    url='http://github.com/ondmagi/pybpdbjobs',
    packages=packages,
    package_dir={'pybpdbjobs': 'pybpdbjobs'},
    requires=requires,
    license=pybpdbjobs.__license__,
    keywords=['netbackup', 'bpdbjobs'],
    classifiers=(
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities',
    )
)