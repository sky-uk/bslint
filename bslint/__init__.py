# -*- coding: utf-8 -*-
"""
    BSLint
    ~~~~~
    A linter for the BrightScript language.
    :license: BSD, see LICENSE for more details.
"""

__version__ = '0.4.10'

from .lexer import Lexer
from .main import get_string_to_parse
from .config_loader import *
from .file_reader import *
from .Handlers.regex_handler import *

from .commands import *
from .bslint import *

