import src.utils
import argparse
from typing import TextIO, Generator


DIGIT = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
LETTERS = list("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
SPECIALS = list("!@#$%^&*(){}[]:\"\\/|;,.<>~")


BASIC_ENUMERATION = [
    [None, DIGIT],
    [DIGIT, None],
    [None, DIGIT, DIGIT],
    [None, DIGIT, DIGIT, DIGIT],
    [None, DIGIT, DIGIT, DIGIT, DIGIT],
    [DIGIT, DIGIT, None],
    [DIGIT, DIGIT, DIGIT, None],
    [DIGIT, DIGIT, DIGIT, DIGIT, None],
    [DIGIT, None, DIGIT],
    [DIGIT, None, DIGIT, DIGIT],
    [DIGIT, DIGIT, None, DIGIT],
    [DIGIT, DIGIT, None, SPECIALS],
    [SPECIALS, None, DIGIT, DIGIT],
    [SPECIALS, DIGIT, None, DIGIT],
    [None, SPECIALS, DIGIT, DIGIT],
    [None, DIGIT, SPECIALS, DIGIT],
    [None, DIGIT, DIGIT, SPECIALS],
    [SPECIALS, DIGIT, DIGIT, None],
    [DIGIT, DIGIT, SPECIALS, None]
]


def enumerate_wordlist_argparse(params: list[str] = "") -> None:
    parser = argparse.ArgumentParser(add_help=False, usage=argparse.SUPPRESS)
    parser.add_argument("infile", type=str)
    parser.add_argument("mode", nargs="?", type=str)
    namespace = parser.parse_args(params)
    namespace.mode = namespace.mode if namespace.mode is not None else "basic"
    with open(namespace.infile) as infile:
        for new_word in enumerate_file(infile, BASIC_ENUMERATION if namespace.mode == "basic" else ADVANCED_ENUMERATION):
            print(new_word)


def enumerate_file(infile: TextIO, enumeration_possibilties: list = None) -> Generator[str, None, None]:
    if enumeration_possibilties is None:
        enumeration_possibilties = BASIC_ENUMERATION

    for line in src.utils.get_next_line(infile):
        for enum in enumeration_possibilties:
            new_enum = [(enu if enu is not None else [line]) for enu in enum]
            for word in src.utils.enumerate_list_of_lists(new_enum, True):
                yield word
