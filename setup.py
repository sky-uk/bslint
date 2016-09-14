# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""

import re
from setuptools import setup, find_packages

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('src/bslint.py').read(),
    re.M
).group(1)

with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")

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

"""
BSLint
-----
BSLint is a linter for the BrightScript language.
"""
# import re
# import ast
# from setuptools import setup
#
#
# _version_re = re.compile(r'__version__\s+=\s+(.*)')
#
# with open('flask/__init__.py', 'rb') as f:
#     version = str(ast.literal_eval(_version_re.search(
#         f.read().decode('utf-8')).group(1)))
#
#
# setup(
#     name='BSLint',
#     version=version,
#     url='https://github.com/sky-uk/bslint/',
#     license='BSD',
#     description='A linter for the BrightScript language.',
#     long_description=__doc__,
#     packages=['bslint'],
#     include_package_data=True,
#     zip_safe=False,
#     platforms='any',
#     install_requires=[
#         'pyenchant>==1.6.8'
#     ],
#     classifiers=[
#         'Development Status :: 4 - Beta',
#         'Environment :: Web Environment',
#         'Intended Audience :: Developers',
#         'License :: OSI Approved :: BSD License',
#         'Operating System :: OS Independent',
#         'Programming Language :: Python',
#         'Programming Language :: Python :: 2',
#         'Programming Language :: Python :: 2.6',
#         'Programming Language :: Python :: 2.7',
#         'Programming Language :: Python :: 3',
#         'Programming Language :: Python :: 3.3',
#         'Programming Language :: Python :: 3.4',
#         'Programming Language :: Python :: 3.5',
#         'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
#         'Topic :: Software Development :: Libraries :: Python Modules'
#     ],
#     entry_points='''
#         [console_scripts]
#         flask=flask.cli:main
#     '''
# )