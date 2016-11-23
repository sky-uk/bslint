import json
import sys
from bslint.messages import print_constants as print_const
from bslint.messages import handler as msg_handler
from filepaths import DEFAULT_CONFIG_FILE_PATH
CONFIG = ""


def load_config_file(user_filepath=None, default_filepath=DEFAULT_CONFIG_FILE_PATH, out=sys.stdout):
    default_json = get_default_config(default_filepath)
    try:
        user_json = get_user_config(user_filepath)
        default_json = overwrite_default_config(default_json, user_json)
    except FileNotFoundError:
        out.write(msg_handler.get_print_msg(print_const.NO_BSLINTRC))
    except ValueError:
        out.write(msg_handler.get_print_msg(print_const.CANNOT_PARSE_BSLINTRC))
        default_json = None
    except IndexError as ex:
        out.write(msg_handler.get_print_msg(print_const.BSLINTRC_KEY_DOSNT_EXIST, [ex.args[0]]))
        default_json = None
    finally:
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
    for setting in user_json:
        if setting not in default_json:
            raise IndexError(setting)
        default_json[setting] = user_json[setting]
    return default_json


def read_json(filepath):
    with open(filepath, 'r') as file:
        return json.loads(file.read())
