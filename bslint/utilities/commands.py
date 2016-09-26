import codecs
import re

import bslint.error_messages_builder.error_builder.error_messages_constants as err_const
import bslint.utilities.config_loader as config_loader
import bslint.utilities.words_dictionary as words_dict
import bslint.constants as const
import bslint.regexs as regexs


comment_regex = [regex[0] for regex in regexs.List if regex[1] == const.COMMENT][0]
dictionary = words_dict._get_new_dictionary()


def check_comment(token):
    if _command_is_active("check_comment") is not True:
        return

    check_comment_config = config_loader.CONFIG["check_comment"]["params"]
    allow_todos = check_comment_config["TODOs"]["allow_TODOs"]
    allow_generic_comments = check_comment_config["allow_generic_comments"]
    todos_format = check_comment_config["TODOs"]["format"]

    if allow_todos and allow_generic_comments:
        if re.match(comment_regex + "TODO", token):
            if not re.match(todos_format, token):
                return {"error_key": err_const.NON_CONVENTIONAL_TODO, "error_params": []}

    elif allow_todos and not allow_generic_comments:
        if not re.match(todos_format, token):
            return {"error_key": err_const.NON_CONVENTIONAL_TODO_AND_NO_COMMENTS, "error_params": []}

    elif not allow_todos and allow_generic_comments:
        if re.match(comment_regex + "TODO", token, re.IGNORECASE):
            return {"error_key": err_const.NO_TODOS, "error_params": []}

    else:
        return {"error_key": err_const.COMMENTS_NOT_ALLOWED, "error_params": []}
    return


def check_file_encoding(file_path):
    if _command_is_active("check_file_encoding") is not True:
        return

    file_encoding = config_loader.CONFIG['check_file_encoding']['params']
    try:
        codecs.open(file_path, encoding=file_encoding["source_file_encoding"]).read()
    except:
        return {"error_key": err_const.FILE_ENCODING, "error_params": []}


def check_indentation(current_indentation_level, characters, indentation_level):
    if _command_is_active("check_indentation") is not True:
        return
    if indentation_level == const.DECREMENT_INDENTATION or \
                    indentation_level == const.SPECIAL_INDENTATION:
        current_indentation_level -= 1
    warning = _handle_warnings(current_indentation_level, characters)
    if indentation_level == const.INCREMENT_INDENTATION or \
                    indentation_level == const.SPECIAL_INDENTATION:
        current_indentation_level += 1

    return warning, current_indentation_level


def check_trace_free():
    if _command_is_active("check_trace_free") is True:
        return {"error_key": err_const.TRACEABLE_CODE, "error_params": []}


def check_max_line_length(line_length):
    if _command_is_active("max_line_length") is not True:
        return

    max_len = config_loader.CONFIG['max_line_length']['params']['max_line_length']
    if max_len < line_length:
        return {"error_key": err_const.LINE_LENGTH, "error_params": [max_len]}


def check_consecutive_empty_lines(empty_lines):
    if _command_is_active("consecutive_empty_lines") is not True:
        return

    params = config_loader.CONFIG["consecutive_empty_lines"]["params"]
    empty_lines_allowed = params["consecutive_empty_lines"]
    if empty_lines > empty_lines_allowed:
        return {"error_key": err_const.CONSECUTIVE_EMPTY_LINES, "error_params": [empty_lines_allowed]}


def check_skip_file():
    if _command_is_active("skip_file") is not True:
        return

    return True


def check_skip_line(line_number):
    if _command_is_active("skip_line") is not True:
        return

    return line_number + 1


def check_spaces_around_operators(characters, current_char_index):
    if _command_is_active("spaces_around_operators") is not True:
        return

    allowed_num_spaces = config_loader.CONFIG["spaces_around_operators"]["params"]["spaces_around_operators"]
    before_index = current_char_index - allowed_num_spaces - 2
    after_index = current_char_index + allowed_num_spaces + 1
    chars_around_operator = characters[before_index:after_index]
    if not re.match("(\S{0,1})\s{" + str(allowed_num_spaces) + "}\S\s{" + str(
            allowed_num_spaces) + "}\S{0,1}$", chars_around_operator):
        return {"error_key": err_const.NO_SPACE_AROUND_OPERATORS,
                "error_params": [allowed_num_spaces]}


def check_spelling(token, token_type):
    if _command_is_active("spell_check") is not True:
        return

    if token_type == const.COMMENT:
        words = _parse_comment_words(token)
    else:
        words = _parse_words(token)

    for word in words:
        spelt_correct = dictionary.check(word)
        if not spelt_correct:
            return {"error_key": err_const.TYPO_IN_CODE, "error_params": []}


def check_method_declaration_spacing(read_line):
    read_line = read_line.lstrip()

    if _command_is_active("check_method_declaration_spacing") is not True or re.match(comment_regex, read_line, re.IGNORECASE):
        return

    method_spaces = config_loader.CONFIG["check_method_declaration_spacing"]["params"]["method_spaces"]

    if re.search(r"\b(function|sub)\b", read_line, re.IGNORECASE) and not re.search(r"\b(end function|end sub)\b",
                                                                     read_line) and not re.search(
        r"\b(endfunction|endsub)\b",
        read_line, re.IGNORECASE):
        if not re.search(r"(function|sub)\s{" + str(method_spaces) + "}[a-z0-9_A-Z]*\(([a-z0-9_A-Z]*" + \
                                 "(?:(\s{" + str(method_spaces) + "}as\s{" + str(
            method_spaces) + "}([a-z0-9_A-Z]+))?)(?:,\s{" + \
                                 str(method_spaces) + "}[a-z0-9_A-Z]*)?)*\)", read_line, re.IGNORECASE):
            return {"error_key": err_const.METHOD_DECLARATION_SPACING, "error_params": []}


# region Private helper functions


def _command_is_active(command_name):
    if command_name in config_loader.CONFIG:
        return config_loader.CONFIG[command_name]["active"]
    else:
        return False


def _change_dict_lang(dict_lang):
    global dictionary
    dictionary = words_dict._get_new_dictionary(dict_lang)


def _handle_warnings(current_indentation_level, characters):
    indent_config = config_loader.CONFIG['check_indentation']['params']
    only_tab_indents = indent_config["only_tab_indents"]
    tab_size = indent_config["tab_size"]
    if re.search(r"\S", characters):
        if only_tab_indents:
            if not re.match("\t{" + str(current_indentation_level) + "}\S", characters):
                return {"error_key": err_const.TAB_AND_SPACES, "error_params": []}
        else:
            if not re.match("\s{" + str(
                            tab_size *
                            current_indentation_level) + "}\S",
                            characters):
                return {"error_key": err_const.TAB_INDENTATION_ERROR,
                        "error_params": [tab_size]}


def _parse_words(identifier_str):
    words = []
    word = ''

    for i in range(0, len(identifier_str)):
        char = identifier_str[i]
        if not char.isalpha():
            if not word == '':
                words.append(word)
            word = ''
            continue
        if char.islower():
            word += char
        elif char.isupper():
            if not word == '':
                words.append(word)
            word = ''
            word += char
        elif char == '_' and word != '':
            words.append(word)
            word = ''
    if not word == '':
        words.append(word)

    return words


def _parse_comment_words(comment):
    words = []
    comment_list = comment.split(' ')

    for word in comment_list:
        if not word.isalpha():
            continue
        if word == 'rem':
            continue
        if word.isupper():
            continue
        else:
            if not word == '':
                words.append(word)
    return words

# endregion
