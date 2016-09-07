import json
import sys


def load_config_file(user='user-config.json', default='default-config.json', out=sys.stdout):
    if sys.argv[0].endswith('nosetests') or sys.argv[0] == 'Main.py':
        user_filepath = "./resources/config/" + user
        default_filepath = "./resources/config/" + default
    else:
        user_filepath = "../resources/config/" + user
        default_filepath = "../resources/config/" + default

    try:
        default_json = read_json(default_filepath)
        user_json = read_json(user_filepath)
        for property in user_json:
            default_json[property] = user_json[property]
    except FileNotFoundError as e:
        out.write("Cannot find file: " + e.filename)
    else:
        #out.write("Read styling config JSON correctly. \n")
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