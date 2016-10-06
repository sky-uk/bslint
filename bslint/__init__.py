# -*- coding: utf-8 -*-
"""
    BSLint
    ~~~~~
    A linter for the BrightScript language.
    :license: BSD, see LICENSE for more details.
"""

__version__ = '0.4.15'

from bslint.lexer.regex_handler import *
from .bslint import *
from .main import get_string_to_parse
from .lexer.commands import *
from .utilities.config_loader import *
from .utilities.file_reader import *


