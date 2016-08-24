import json
import sys


def load_config_file(out=sys.stdout):
    default_filepath = "../resources/config/default-config.json"
    user_filepath = "../resources/config/user-config.json"

    try:
        default_json = read_json(default_filepath)
        user_json = read_json(user_filepath)
        for property in user_json:
            default_json[property] = user_json[property]
    except FileNotFoundError as e:
        out.write("Cannot find file: " + e.filename)
    else:
        out.write("Read styling config JSON correctly.")
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