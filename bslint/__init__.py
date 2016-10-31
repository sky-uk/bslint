# -*- coding: utf-8 -*-
"""
    BSLint
    ~~~~~
    A linter for the BrightScript language.
    :license: BSD, see LICENSE for more details.
"""

# pylint: disable=wildcard-import

from bslint.lexer.commands import *
from bslint.lexer.handlers.regex_handler import find_match
from .bslint import *
from .utilities.config_loader import *
