import json
import os
import sys

from filepaths import DEFAULT_CONFIG_FILE_PATH
CONFIG = ""


def load_config_file(user_filepath=None, default_filepath=DEFAULT_CONFIG_FILE_PATH, out=sys.stdout):

    try:
        default_json = get_default_config(default_filepath)
        user_json = get_user_config(user_filepath)
        overwrite_default_config(default_json, user_json)
    except FileNotFoundError as e:
        out.write("Cannot find file: " + os.path.basename(e.filename))
    else:
        global CONFIG
        CONFIG = default_json
        return default_json


def get_default_config(default_filepath):
    return read_json(default_filepath)


def get_user_config(user_filepath):
    user_json = ""
    if user_filepath is not None:
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
