import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(os.path.dirname(current))
sys.path.append(parent)

import src.utils
import src.enumerate


# this file will takes up like 1+ gb lol
APPEND_DIGIT = [f"${_2}" for _2 in "0123456789"]


def main():
    rulegen = [APPEND_DIGIT] * 8
    for _ in src.utils.enumerate_list_of_lists(rulegen):
        print(_)


if __name__ == '__main__':
    main()
