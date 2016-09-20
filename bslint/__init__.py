# -*- coding: utf-8 -*-
"""
    BSLint
    ~~~~~
    A linter for the BrightScript language.
    :license: BSD, see LICENSE for more details.
"""

__version__ = '0.4.15'

from .utilities.commands import *
from .utilities.config_loader import *
from .utilities.file_reader import *
from .utilities.regex_handler import *
from .bslint import *
from .lexer import lex
from .main import get_string_to_parse

