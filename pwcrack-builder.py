#!/usr/bin/python3

import sys
import src


def generic_help_message(say=False):
    help_msg = "Usage: python3 pwcrack-builder <tool> [args]"
    return help_msg if say else print(help_msg)


def main():
    assert len(sys.argv) != 0, "What? How???"
    assert len(sys.argv) != 1, "Usage: python3 pwcrack-builder <tool> [args]"

    tool = sys.argv[1]
    params = " ".join(sys.argv[2:])

    tool_mapping = {
        "help": generic_help_message(),
        "expand": lambda _: None
    }


if __name__ == '__main__':
    main()
