# -*- coding: utf-8 -*-
"""
    BSLint
    ~~~~~
    A linter for the BrightScript language.
    :license: BSD, see LICENSE for more details.
"""

from bslint.lexer.regex_handler import *
from .bslint import *
from .main import get_string_to_parse
from .lexer.commands import *
from .utilities.config_loader import *


