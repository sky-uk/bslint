from .lexer import Lexer
from .main import main
from .config_loader import *
from .styling_rules_handler import *
from .file_reader import *
from .Handlers.regex_handler import *

from .BSLINT_commands.skip_line_command import *
from .BSLINT_commands.skip_file_command import *
from .BSLINT_commands.check_comment_command import *
from .BSLINT_commands.spell_check_command import *
from .BSLINT_commands.max_line_length_command import *
from .BSLINT_commands.check_indentation_command import *
from .BSLINT_commands.consecutive_empty_lines_command import *
from .BSLINT_commands.check_trace_free_command import *
from .BSLINT_commands.check_file_encoding_command import *
from .BSLINT_commands.spaces_around_operators_command import *
