"""bslint.bslint: provides entry point main()."""
import sys
import os
from bslint.interface_handler import InterfaceHandler as InterfaceHandler

__version__ = "0.6.1"


def main():
    try:
        interface_handler = InterfaceHandler()
        interface_handler.main()
    except KeyboardInterrupt:
        pass


def runner(to_lex=None):
    sys.argv = [sys.argv[0]]
    if to_lex is not None:
        sys.argv.append(os.path.abspath(to_lex))
    else:
        sys.argv.append(os.getcwd())
    interface_handler = InterfaceHandler()
    interface_handler.main()
    return interface_handler
