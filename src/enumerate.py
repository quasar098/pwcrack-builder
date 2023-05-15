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
    [DIGIT, None, LETTER],
    [LETTER, SPECIAL, DIGIT, None],
    [SPECIAL, LETTER, DIGIT, None],
    [DIGIT, SPECIAL, LETTER, None],
    [SPECIAL, DIGIT, LETTER, None],
    [LETTER, DIGIT, SPECIAL, None],
    [DIGIT, LETTER, SPECIAL, None],
    [None, LETTER, SPECIAL, DIGIT],
    [None, SPECIAL, LETTER, DIGIT],
    [None, DIGIT, SPECIAL, LETTER],
    [None, SPECIAL, DIGIT, LETTER],
    [None, LETTER, DIGIT, SPECIAL],
    [None, DIGIT, LETTER, SPECIAL]
]

# BASIC_ENUMERATION = [
#     [SPECIAL, DIGIT, None, DIGIT]
# ]


def enumerate_wordlist(infile: TextIO, enumeration_possibilties: list = None, remove_duplicates=True) -> Generator[str, None, None]:
    """Enumerate all the passwords in an entire file"""
    seen = set()
    for line in src.utils.get_next_line(infile):
        for new in enumerate_password(line, enumeration_possibilties, remove_duplicates=remove_duplicates):
            if remove_duplicates:
                if new not in seen:
                    seen.add(new)
                    yield new
            else:
                yield new


def enumerate_password(original: str, enumeration_possibilities=None, remove_duplicates=True):
    """Enumerate a single password"""
    if enumeration_possibilities is None:
        enumeration_possibilities = BASIC_ENUMERATION
    seen = set()
    for enum in enumeration_possibilities:
        new_enum = [(enu if enu is not None else [original]) for enu in enum]
        for word in src.utils.enumerate_list_of_lists(new_enum, True):
            if remove_duplicates:
                if word not in seen:
                    seen.add(word)
                    yield word
            else:
                yield word
