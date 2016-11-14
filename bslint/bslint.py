"""bslint.bslint: provides entry point main()."""
import sys
import os
from multiprocessing import Pipe
from bslint.interface_handler import InterfaceHandler as InterfaceHandler

__version__ = "0.6.2"


def main():
    try:
        interface_handler = InterfaceHandler()
        interface_handler.start()
    except KeyboardInterrupt:
        pass


def runner(to_lex=None, out=sys.stdout):
    sys.argv = [sys.argv[0]]
    if to_lex is not None:
        sys.argv.append("--path")
        sys.argv.append(os.path.abspath(to_lex))
        sys.argv.append("--lex")
    parent_conn, child_conn = Pipe()
    interface_handler = InterfaceHandler(out=out, conn=child_conn)
    interface_handler.start()
    setup_test_data(interface_handler, parent_conn)
    return interface_handler


def setup_test_data(interface_handler, parent_conn):
    test_dict = parent_conn.recv()
    interface_handler.messages = test_dict["messages"]
    interface_handler.files = test_dict["files"]
    interface_handler.printed_output = test_dict["printed_output"]
    interface_handler.config = test_dict["config"]
    interface_handler.join()
