# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""

import re
from setuptools import setup, find_packages
import pip

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('src/bslint.py').read(),
    re.M
).group(1)

with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")

pip.main(['install', 'pyenchant'])

setup(

    name = "bslint",
    packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_data={'src': ['config/*.json', 'config/personal-words-list.txt']},
    entry_points = { "console_scripts": ['bslint = src.bslint:main'] },
    version = version,
    description = "A linter tool for the BrightScript language.",
    long_description = long_descr,
    author = "BSLint",
    author_email="zachary.robinson@sky.uk",
    url = "https://github.com/sky-uk/bslint",
    download_url='https://github.com/sky-uk/bslint/archive/0.2.4.tar.gz',
    )