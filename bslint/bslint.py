"""bslint.bslint: provides entry point main()."""
__version__ = "0.6.0"

import os
import sys

import bslint
import bslint.constants as const
import bslint.lexer as lexer

is_lexed_correctly = True
files = []


def main():
    print(const.TITLE_COLOUR + "BSLint: A linter for BrightScript. %s. \n" % __version__ + const.END_COLOUR)
    global is_lexed_correctly
    try:
        manifest_path = find_manifest()
    except FileNotFoundError:
        manifest_path = ""
        print(const.ERROR_COLOUR + "No manifest file found" + const.END_COLOUR)

    try:
        bslintrc_path = os.path.join(manifest_path, ".bslintrc")
        bslintrc = read_bslintrc(bslintrc_path)
        bslint.config_loader.load_config_file(bslintrc_path)
    except FileNotFoundError:
        print(const.ERROR_COLOUR + "No .bslintrc file found" + const.END_COLOUR)
        bslintrc = {"ignore": ""}

    if is_not_specific_path():
        pathname = os.getcwd()
        lint_all(pathname, bslintrc["ignore"], manifest_path)
    else:
        filename = sys.argv[1]
        if not os.path.exists(filename):
            is_lexed_correctly = False

        if os.path.isfile(filename):
            lint_specific(filename)
        else:
            lint_all(filename, bslintrc["ignore"], manifest_path)
    if is_lexed_correctly:
        print(const.PASS_COLOUR + 'All lexed correctly' + const.END_COLOUR)
        print("\n")


def lint_all(directory, directories_to_ignore, manifest_path):
    for dirName, subdirList, files in os.walk(directory):
        if not ignore_dir(get_relative_path(dirName, manifest_path), directories_to_ignore):
            for file in files:
                if file.endswith(".brs") or file.endswith(".bs"):
                    filepath = os.path.join(dirName, file)
                    lint_specific(filepath)


def get_relative_path(dirName, directory):
    directory = os.path.realpath(os.path.join(os.getcwd(), directory))
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
    while no_manifest_in_folder(upper_dir) and count < 5:
        upper_dir = os.path.join(upper_dir, "../")
        count += 1
    if count == 5:
        raise FileNotFoundError
    return upper_dir


def no_manifest_in_folder(upper_dir):
    return not os.path.exists(os.path.join(upper_dir, "MANIFEST")) and not os.path.exists(
        os.path.join(upper_dir, "manifest"))


def read_bslintrc(manifest_dir):
    if manifest_dir is not None:
        bslintrc = bslint.config_loader.read_json(manifest_dir)
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