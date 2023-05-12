import src.utils
import argparse
from typing import TextIO, Generator


DIGIT = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
LETTER = list("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
SPECIAL = list("!@#$%^&*(){}[]:\"\\/|;,.<>~")


BASIC_ENUMERATION = [
    [None, DIGIT],
    [DIGIT, None],
    [SPECIAL, None],
    [None, SPECIAL],
    [None, None],
    [None, SPECIAL, None],
    [None, DIGIT, None],
    [SPECIAL, SPECIAL, None],
    [None, SPECIAL, SPECIAL],
    [DIGIT, None, SPECIAL],
    [SPECIAL, None, DIGIT],
    [None, DIGIT, DIGIT],
    [None, DIGIT, DIGIT, DIGIT],
    [None, DIGIT, DIGIT, DIGIT, DIGIT],
    [DIGIT, DIGIT, None],
    [DIGIT, DIGIT, DIGIT, None],
    [DIGIT, DIGIT, DIGIT, DIGIT, None],
    [DIGIT, None, DIGIT],
    [DIGIT, None, DIGIT, DIGIT],
    [DIGIT, DIGIT, None, DIGIT],
    [DIGIT, DIGIT, None, SPECIAL],
    [SPECIAL, None, DIGIT, DIGIT],
    [SPECIAL, DIGIT, None, DIGIT],
    [None, SPECIAL, DIGIT, DIGIT],
    [None, DIGIT, SPECIAL, DIGIT],
    [None, DIGIT, DIGIT, SPECIAL],
    [SPECIAL, DIGIT, DIGIT, None],
    [DIGIT, DIGIT, SPECIAL, None],
    [DIGIT, DIGIT, None, DIGIT, DIGIT],
    [LETTER, None],
    [None, LETTER],
    [None, LETTER, LETTER],
    [LETTER, LETTER, None],
    [LETTER, None, LETTER],
    [None, DIGIT, LETTER],
    [None, LETTER, DIGIT],
    [None, SPECIAL, LETTER],
    [None, LETTER, SPECIAL],
    [DIGIT, LETTER, None],
    [LETTER, DIGIT, None],
    [SPECIAL, LETTER, None],
    [LETTER, SPECIAL, None],
    [LETTER, None, SPECIAL],
    [SPECIAL, None, LETTER],
    [LETTER, None, DIGIT],
    [DIGIT, None, LETTER]
]


def enumerate_wordlist_argparse(params: list[str] = "") -> Generator[str, None, None]:
    parser = argparse.ArgumentParser(add_help=False, usage=argparse.SUPPRESS)
    parser.add_argument("infile", type=str)
    parser.add_argument("--debug", action="store_true")
    namespace = parser.parse_args(params)
    with open(namespace.infile) as infile:
        for new_word in enumerate_file(
            infile,
            BASIC_ENUMERATION,
            debug=namespace.debug
        ):
            yield new_word


def enumerate_file(infile: TextIO, enumeration_possibilties: list = None, debug=False) -> Generator[str, None, None]:
    total_enums = 0
    total_lines = 0
    if enumeration_possibilties is None:
        enumeration_possibilties = BASIC_ENUMERATION

    for line in src.utils.get_next_line(infile):
        total_lines += 1
        for enum in enumeration_possibilties:
            new_enum = [(enu if enu is not None else [line]) for enu in enum]
            for word in src.utils.enumerate_list_of_lists(new_enum, True):
                yield word
                total_enums += 1
    if debug:
        print(f"Total: {total_enums} from {total_lines} (~{int(total_enums/total_lines)} per)")
