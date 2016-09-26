import json
import sys
import os

CONFIG = ""


def load_config_file(user_filepath=None, default_filepath=None, out=sys.stdout):
    this_dir, this_filename = os.path.split(__file__)
    tests_filepath_prefix = os.path.join(this_dir, "../../tests/resources/config/")
    filepath_prefix = os.path.join(this_dir, "../../bslint/config/")

    try:
        default_json = get_default_config(default_filepath, filepath_prefix, tests_filepath_prefix)
        user_json = get_user_config(tests_filepath_prefix, user_filepath)
        overwrite_default_config(default_json, user_json)
    except FileNotFoundError as e:
        out.write("Cannot find file: " + e.filename)
    else:
        global CONFIG
        CONFIG = default_json
        return default_json


def get_default_config(default, filepath_prefix, tests_filepath_prefix):
    if default:
        default_filepath = tests_filepath_prefix + default
    else:
        default_filepath = filepath_prefix + "default-config.json"
    return read_json(default_filepath)


def get_user_config(tests_filepath_prefix, user_filepath):
    user_json = ""
    print(user_filepath)
    if user_filepath is not None:
        if not os.path.isfile(user_filepath):
            user_filepath = tests_filepath_prefix + user_filepath
        print(user_filepath)
        user_json = read_json(user_filepath)
    return user_json


def overwrite_default_config(default_json, user_json):
    for property in user_json:
        default_json[property] = user_json[property]
    return default_json


def read_json(filepath):
    config_string = ''
    with open(filepath) as f:
        for line in f:
            line = line.lstrip()
            if not line.startswith("//"):
                config_string += line
    config_json = json.loads(config_string)
    return config_json


if __name__ == "__main__":
    load_config_file()