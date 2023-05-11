#!/usr/bin/python3

import sys

import src.expand_wordlist


# noinspection PyUnusedLocal
def generic_help_message(params: list[str] = None):
    help_msg = "Usage: python3 pwcrack-builder <tool> [args]"
    help_msg += "\nPossible tools: expand"
    print(help_msg)


# noinspection PyArgumentList
def main():
    assert len(sys.argv) != 0, "What? How???"
    if len(sys.argv) == 1:
        generic_help_message()
        quit()

    tool = sys.argv[1]
    params = sys.argv[2:]

    tool_mapping = {
        "expand": src.expand_wordlist.expand_wordlist_argparse
    }

    tool_mapping.get(tool, generic_help_message)(params)


if __name__ == '__main__':
    main()
