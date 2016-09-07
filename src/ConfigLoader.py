import json
import sys
import pkgutil


def load_config_file(user=None, default=None, out=sys.stdout):
    if sys.argv[0].endswith('bslint'):
        user_json = pkgutil.get_data('src', 'config/user-config.json')
        default_json = pkgutil.get_data('src', 'config/default-config(actual).json')

        user_json = json.loads(user_json.decode('ascii'))
        default_json = json.loads(default_json.decode('ascii'))

        for property in user_json:
            default_json[property] = user_json[property]
        return default_json

    elif sys.argv[0].endswith('nosetests') or sys.argv[0] == 'Main.py':
        if user:
            user_filepath = "./resources/config/" + user
        else:
            user_filepath = "./src/config/user-config.json"
        if default:
            default_filepath = "./resources/config/" + default
        else:
            default_filepath = "./src/config/default-config.json"
    else:
        if user:
            user_filepath = "../resources/config/" + user
        else:
            user_filepath = "../src/config/user-config.json"
        if default:
            default_filepath = "../resources/config/" + default
        else:
            default_filepath = "../src/config/default-config.json"

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

if __name__ == "__main__":
    load_config_file()