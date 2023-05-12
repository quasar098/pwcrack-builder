import src.utils
import argparse
from typing import TextIO, Generator


def do_stuff_argparse(params: list[str] = "") -> Generator[str, None, None]:
    parser = argparse.ArgumentParser(add_help=False, usage=argparse.SUPPRESS)
    parser.add_argument("infile", type=str)
    parser.add_argument("--debug", action="store_true")
    namespace = parser.parse_args(params)
    with open(namespace.infile) as infile:
        for new_word in do_stuff_file(infile, debug=namespace.debug):
            yield new_word


def do_stuff_file(infile: TextIO, debug=False) -> Generator[str, None, None]:
    pass
