import src


def main(filepath):
    fo = open(filepath, "r+")
    str_to_parse = fo.read()

    return str_to_parse
