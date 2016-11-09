"""bslint.bslint: provides entry point main()."""
import sys
import os
from bslint.interface_handler import InterfaceHandler as InterfaceHandler

__version__ = "0.6.2"


def main():
    try:
        interface_handler = InterfaceHandler()
        interface_handler.main()
    except KeyboardInterrupt:
        pass


def runner(to_lex=None, out=sys.stdout):
    sys.argv = [sys.argv[0]]
    if to_lex is not None:
        sys.argv.append("--path")
        sys.argv.append(os.path.abspath(to_lex))
    interface_handler = InterfaceHandler(out=out)
    interface_handler.main()
    return interface_handler
