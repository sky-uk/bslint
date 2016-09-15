"""bslint.bslint: provides entry point main()."""
__version__ = "0.3.8"


import os
import sys

import bslint
import bslint.constants as const

is_lexed_correctly = True
files = []


def main():
    print(const.TITLE_COLOUR + "BSLint: A linter for BrightScript. %s. \n" % __version__ + const.END_COLOUR)
    global is_lexed_correctly
    try:
        manifest_path = find_manifest()
    except FileNotFoundError:
        manifest_path = None
        print(const.ERROR_COLOUR + "No manifest file found" + const.END_COLOUR)

    try:
        bslintrc = read_bslintrc(manifest_path)
    except FileNotFoundError:
        print(const.ERROR_COLOUR + "No .bslintrc file found" + const.END_COLOUR)
        bslintrc = {"ignore": ""}

    if is_not_specific_path():
        pathname = sys.argv
        lint_all(pathname, bslintrc["ignore"])
    else:
        filename = sys.argv[1]
        if not os.path.exists(filename):
            is_lexed_correctly = False

        if os.path.isfile(filename):
            lint_specific(filename)
        else:
            lint_all(filename, bslintrc["ignore"])
    if is_lexed_correctly:
        print(const.PASS_COLOUR + 'All lexed correctly' + const.END_COLOUR)
        print("\n")


def lint_all(directory, directories_to_ignore):
    for dirName, subdirList, files in os.walk(directory):
        if not ignore_dir(get_relative_path(dirName, directory), directories_to_ignore):
            for file in files:
                if file.endswith(".brs") or file.endswith(".bs"):
                    filepath = os.path.join(dirName, file)
                    lint_specific(filepath)


def get_relative_path(dirName, directory):
    return dirName.replace(directory, '')


def ignore_dir(relative_directory_path, directories_to_ignore):
    for directory in directories_to_ignore:
        directory = add_slashes_to_dir(directory)
        relative_directory_path = add_slashes_to_dir(relative_directory_path)
        if relative_directory_path.startswith(directory):
            return True
    return False


def add_slashes_to_dir(directory):
    if not directory.startswith("/"):
        directory = "/" + directory
    if not directory.endswith("/"):
        directory += "/"
    return directory


def lint_specific(filename):
    filename = filename.replace(os.getcwd() + '/', '')
    if filename.endswith(".brs") or filename.endswith(".bs"):
        files.append(filename)
        file_reader = bslint.FileReader()
        read_file = file_reader.read_file(filename)
        lexer = bslint.Lexer()
        if read_file["invalid_encoding"]:
            print(read_file["invalid_encoding"])

        lex_result = lexer.lex(read_file['str_to_lex'])
        if lex_result["Status"] == "Error" or lex_result["Warnings"]:
            global is_lexed_correctly
            is_lexed_correctly = False
            print(const.FILE_COLOUR + filename + const.END_COLOUR)
            if lex_result["Status"] == "Error":
                for error in lex_result["Tokens"]:
                    print(const.ERROR_COLOUR + str(error) + const.END_COLOUR)
            for warning in lex_result["Warnings"]:
                print(const.WARNING_COLOUR + str(warning) + const.END_COLOUR)
            print("\n")
    else:
        is_lexed_correctly = False


def find_manifest():
    if is_not_specific_path():
        upper_dir = ""
    else:
        if os.path.isfile(sys.argv[1]):
            upper_dir = os.path.dirname(sys.argv[1])
        else:
            upper_dir = sys.argv[1]
    count = 0
    manifest_path_upper = os.path.join(upper_dir, "MANIFEST")
    manifest_path_lower = os.path.join(upper_dir, "manifest")
    while not os.path.exists(manifest_path_upper) and not os.path.exists(manifest_path_lower) and count < 5:
        upper_dir += "../"
        count += 1
    if count == 5:
        raise FileNotFoundError
    return upper_dir


def read_bslintrc(manifest_dir):
    if manifest_dir is not None:
        bslintrc = bslint.config_loader.read_json(os.path.join(manifest_dir, ".bslintrc"))
    else:
        raise FileNotFoundError
    return bslintrc


def runner(to_lex=None):
    global files
    files = []
    sys.argv = [sys.argv[0]]
    if to_lex is not None:
        sys.argv.append(os.path.join(os.getcwd(), to_lex))
    else:
        sys.argv.append(os.getcwd())
    main()
    return files


def is_not_specific_path():
    return len(sys.argv) == 1