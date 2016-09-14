# -*- coding: utf-8 -*-
"""
BSLint
-----
BSLint is a linter for the BrightScript language.
"""

import ast
import re
from setuptools import setup, find_packages

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('bslint/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")

setup(
    name = "bslint",
    packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_data={'bslint': ['config/*.json', 'config/personal-words-list.txt']},
    entry_points = { "console_scripts": ['bslint = bslint.bslint:main'] },
    version = version,
    description = "A linter tool for the BrightScript language.",
    long_description = long_descr,
    author = "BSLint",
    author_email="zachary.robinson@sky.uk",
    url = "https://github.com/sky-uk/bslint",
    download_url='https://github.com/sky-uk/bslint/archive/0.2.4.tar.gz',
    install_requires=['pyenchant==1.6.8']
    )