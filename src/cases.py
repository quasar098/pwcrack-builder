import src.utils
import argparse
from typing import TextIO, Generator


DIGIT = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
LETTER = list("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
SPECIAL = list("!@#$%^&*(){}[]:\"\\/|;,.<>~-_=")


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

# BASIC_ENUMERATION = [
#     [SPECIAL, DIGIT, None, DIGIT]
# ]


def cases_wordlist(infile: TextIO) -> Generator[str, None, None]:
    """Enumerate cases for all the passwords in an entire file"""
    for line in src.utils.get_next_line(infile):
        for new in cases_password(line):
            yield new


def cases_password(original: str, remove_duplicates=False, max_caps=5) -> Generator[str, None, None]:
    """Enumerate cases for a single password"""

    def toggle_the_cases(word: str, indexes_to_toggle: list[int]) -> str:
        new_word = []
        for toggle_index, letter in enumerate(word):
            if toggle_index in indexes_to_toggle:
                new_word.append(letter.upper())
            else:
                new_word.append(letter.lower())
        return "".join(new_word)

    yield original
    seen = set()
    for how_many_toggle in range(1, max_caps):
        # screw you to anyone who says 'indicies' 🤓 nerd
        do_toggle = [0] * how_many_toggle
        while True:
            for do_toggle_index in range(len(do_toggle)):
                if do_toggle_index == 0:
                    begin = toggle_the_cases(original, do_toggle)
                    if remove_duplicates:
                        if begin not in seen:
                            seen.add(begin)
                            yield begin
                    else:
                        yield begin
                do_toggle[do_toggle_index] += 1
                if do_toggle[do_toggle_index] == len(original):
                    do_toggle[do_toggle_index] = 0
                    continue
                break
            else:
                break
