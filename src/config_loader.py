import json
import sys
import os


def load_config_file(user=None, default=None, out=sys.stdout):
    this_dir, this_filename = os.path.split(__file__)
    tests_filepath_prefix = os.path.join(this_dir, "../tests/config/")
    filepath_prefix = os.path.join(this_dir, "../src/config/")

    if user:
        user_filepath = tests_filepath_prefix + user
    else:
        user_filepath = filepath_prefix + "user-config.json"
    if default:
        default_filepath = tests_filepath_prefix + default
    else:
        default_filepath = filepath_prefix + "default-config.json"

    try:
        default_json = read_json(default_filepath)
        user_json = read_json(user_filepath)
        for property in user_json:
            default_json[property] = user_json[property]
    except FileNotFoundError as e:
        out.write("Cannot find file: " + e.filename)
    else:
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

CONFIG = load_config_file()

if __name__ == "__main__":
    load_config_file()