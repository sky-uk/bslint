# -*- coding: utf-8 -*-
"""
BSLint
-----
BSLint is a linter for the BrightScript language.
"""

import re
from setuptools import setup, find_packages

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('bslint/bslint.py').read(),
    re.M
).group(1)

setup(
    name="bslint",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_data={'bslint': ['config/*.json', 'config/personal-words-list.txt']},
    entry_points={"console_scripts": ['bslint = bslint.bslint:main']},
    version=version,
    description="A linter tool for the BrightScript language.",
    author="BSLint",
    author_email="zachary.robinson@sky.uk",
    url="https://github.com/sky-uk/bslint",
    install_requires=['pyenchant==1.6.8']
)
