import codecs
import re

import bslint.constants as const
import bslint.messages.error_constants as err_const
import bslint.lexer.regexs as regexs
import bslint.lexer.words_dictionary as words_dict
import bslint.utilities.config_loader as config_loader

COMMENT_REGEX = [regex.regex for regex in regexs.REGEXS if regex.lexer_type == const.COMMENT][0]
DICTIONARY = words_dict.get_new_dictionary()


def check_commas_in_objects():
    if not _command_is_active(const.CHECK_COMMAS_IN_OBJECT):
        return
    return {const.ERROR_KEY: err_const.COMMAS_IN_OBJECTS, const.ERROR_PARAMS: []}


def check_trailing_comma_in_objects():
    if not _command_is_active(const.CHECK_TRAILING_COMMA_IN_OBJECT):
        return
    return {const.ERROR_KEY: err_const.TRAILING_COMMA_IN_OBJECTS, const.ERROR_PARAMS: []}


def check_comment(token):
    if not _command_is_active(const.CHECK_COMMENT):
        return

    check_comment_config = config_loader.CONFIG[const.CHECK_COMMENT][const.PARAMS]
    allow_todos = check_comment_config[const.TODOS][const.ALLOW_TODOS]
    allow_generic_comments = check_comment_config[const.ALLOW_GENERIC_COMMENTS]
    todos_format = check_comment_config[const.TODOS][const.FORMAT]

    return_message = None
    if allow_todos and allow_generic_comments:
        return_message = _check_comment_and_todos(return_message, todos_format, token)

    elif allow_todos and not allow_generic_comments:
        return_message = _check_only_todos(return_message, todos_format, token)

    elif not allow_todos and allow_generic_comments:
        return_message = _check_only_generic_comments(return_message, token)

    else:
        return_message = {const.ERROR_KEY: err_const.COMMENTS_NOT_ALLOWED, const.ERROR_PARAMS: []}
    return return_message


def check_file_encoding(file_path):
    if not _command_is_active(const.CHECK_FILE_ENCODING):
        return

    file_encoding = config_loader.CONFIG[const.CHECK_FILE_ENCODING][const.PARAMS]
    try:
        codecs.open(file_path, encoding=file_encoding[const.SOURCE_FILE_ENCODING]).read()
    except ValueError:
        return {const.ERROR_KEY: err_const.FILE_ENCODING, const.ERROR_PARAMS: []}


def check_indentation(current_indentation_level, characters, indentation_level):
    if not _command_is_active(const.CHECK_INDENTATION) or not len(characters) > 0:
        return

    if indentation_level == const.DECREMENT_INDENTATION or indentation_level == const.SPECIAL_INDENTATION:
        current_indentation_level -= 1
    warning = _check_indentation(current_indentation_level, characters)
    if re.match(r"(\s*)if (.+) then(\s+)(\S)", characters, re.IGNORECASE):
        current_indentation_level -= 1
    if indentation_level == const.INCREMENT_INDENTATION or indentation_level == const.SPECIAL_INDENTATION:
        current_indentation_level += 1

    return warning, current_indentation_level


def check_trace_free():
    if _command_is_active(const.CHECK_TRACE_FREE):
        return {const.ERROR_KEY: err_const.TRACEABLE_CODE, const.ERROR_PARAMS: []}


def check_max_line_length(line_length):
    if not _command_is_active(const.MAX_LINE_LENGTH):
        return

    max_len = config_loader.CONFIG[const.MAX_LINE_LENGTH][const.PARAMS][const.MAX_LINE_LENGTH]
    if max_len < line_length:
        return {const.ERROR_KEY: err_const.LINE_LENGTH, const.ERROR_PARAMS: [max_len]}


def check_consecutive_empty_lines(empty_lines):
    if not _command_is_active(const.CONSECUTIVE_EMPTY_LINES):
        return

    params = config_loader.CONFIG[const.CONSECUTIVE_EMPTY_LINES][const.PARAMS]
    empty_lines_allowed = params[const.CONSECUTIVE_EMPTY_LINES]
    if empty_lines > empty_lines_allowed:
        return {const.ERROR_KEY: err_const.CONSECUTIVE_EMPTY_LINES, const.ERROR_PARAMS: [empty_lines_allowed]}


def check_skip_file():
    return _command_is_active(const.SKIP_FILE)


def check_skip_line(line_number):
    if not _command_is_active(const.SKIP_LINE):
        return
    return line_number + 1


def check_spaces_around_operators(characters, current_char_index):
    if not _command_is_active(const.SPACES_AROUND_OPERATORS):
        return
    allowed_spaces = config_loader.CONFIG[const.SPACES_AROUND_OPERATORS][const.PARAMS][const.SPACES_AROUND_OPERATORS]
    before_index = current_char_index - allowed_spaces - 2
    after_index = current_char_index + allowed_spaces + 1
    chars_around_operator = characters[before_index:after_index]
    if not re.match(r"(\S{0,1})\s{" + str(allowed_spaces) + r"}\S\s{" + str(
            allowed_spaces) + r"}\S{0,1}$", chars_around_operator):
        return {const.ERROR_KEY: err_const.NO_SPACE_AROUND_OPERATORS, const.ERROR_PARAMS: [allowed_spaces]}


def check_spelling(token, token_lexer_type):
    if not _command_is_active(const.SPELL_CHECK):
        return

    if token_lexer_type == const.COMMENT:
        words = _parse_comment_words(token)
    else:
        words = _parse_words(token)

    for word in words:
        spelt_correct = DICTIONARY.check(word)
        if not spelt_correct:
            return {const.ERROR_KEY: err_const.TYPO_IN_CODE, const.ERROR_PARAMS: []}


def check_method_dec_spacing(read_line):
    if not _command_is_active(const.CHECK_METHOD_DECLARATION_SPACING) or COMMENT_REGEX.match(read_line):
        return
    read_line = read_line.lstrip()
    method_spaces = str(config_loader.CONFIG[const.CHECK_METHOD_DECLARATION_SPACING][const.PARAMS][const.METHOD_SPACES])
    if not re.match(r"(function|sub)\s{" + method_spaces + r"}[a-z0-9_]+\(([a-z0-9_]+"
                    + r"(?:(\s{" + method_spaces + r"}as\s{" + method_spaces + r"}([a-z0-9_]+))?)(?:,\s{"
                    + method_spaces + r"}[a-z0-9_]*)?)*\)", read_line, re.IGNORECASE):
        return {const.ERROR_KEY: err_const.METHOD_DECLARATION_SPACING, const.ERROR_PARAMS: []}


def check_trailing_white_space(last_read_line):
    if not _command_is_active(const.TRAILING_WHITE_SPACE):
        return
    if last_read_line != "" and last_read_line[-1] == " ":
        return {const.ERROR_KEY: err_const.TRAILING_WHITE_SPACE, const.ERROR_PARAMS: []}


def change_dict_lang(dict_lang):
    global DICTIONARY
    DICTIONARY = words_dict.get_new_dictionary(dict_lang)

# region Private helper functions


def _check_only_generic_comments(return_message, token):
    matching_string = re.compile(COMMENT_REGEX.pattern + "TODO", re.IGNORECASE)
    if matching_string.match(token):
        return_message = {const.ERROR_KEY: err_const.NO_TODOS, const.ERROR_PARAMS: []}
    return return_message


def _check_only_todos(return_message, todos_format, token):
    if not re.match(todos_format, token):
        return_message = {const.ERROR_KEY: err_const.NON_CONVENTIONAL_TODO_AND_NO_COMMENTS, const.ERROR_PARAMS: []}
    return return_message


def _check_comment_and_todos(return_message, todos_format, token):
    matching_string = re.compile(COMMENT_REGEX.pattern + "TODO")
    if matching_string.match(token):
        if not re.match(todos_format, token):
            return_message = {const.ERROR_KEY: err_const.NON_CONVENTIONAL_TODO, const.ERROR_PARAMS: []}
    return return_message


def _command_is_active(command_name):
    if command_name in config_loader.CONFIG:
        return config_loader.CONFIG[command_name][const.ACTIVE]
    else:
        return False


def _check_indentation(current_indentation_level, characters):
    indent_config = config_loader.CONFIG[const.CHECK_INDENTATION][const.PARAMS]
    tab_size = indent_config[const.TAB_SIZE]
    if indent_config[const.ONLY_TAB_INDENTS]:
        if not re.match(r"\t{" + str(current_indentation_level) + r"}\S", characters):
            return {const.ERROR_KEY: err_const.TAB_AND_SPACES, const.ERROR_PARAMS: []}
    else:
        if not re.match(r"\s{" + str(tab_size * current_indentation_level) + r"}\S", characters):
            return {const.ERROR_KEY: err_const.TAB_INDENTATION_ERROR, const.ERROR_PARAMS: [tab_size]}


def _parse_words(identifier_str):
    words = []
    word = ''

    for i in range(0, len(identifier_str)):
        char = identifier_str[i]
        if not char.isalpha():
            if word != '':
                words.append(word)
            word = ''
            continue
        if char.islower():
            word += char
        elif char.isupper():
            if word != '':
                words.append(word)
            word = ''
            word += char
    if word != '':
        words.append(word)

    return words


def _parse_comment_words(comment):
    words = []
    comment_list = comment.split(' ')

    for word in comment_list:
        if not word.isalpha():
            continue
        if word == const.REM:
            continue
        if word.isupper():
            continue
        else:
            if word != '':
                words.append(word)
    return words

# endregion
