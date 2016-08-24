import json


def load_config_file():
    default_filepath = "../resources/config/default-config.json"
    user_filepath = "../resources/config/user-config.json"

    try:
        default_json = read_json(default_filepath)
        user_json = read_json(user_filepath)
        for property in user_json:
            default_json[property] = user_json[property]
            print(default_json[property])
    except IOError:
        print("Error: cannot find file or read data.")
    else:
        print("Read styling config JSON correctly.")


def read_json(filepath):
    config_json = ''
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