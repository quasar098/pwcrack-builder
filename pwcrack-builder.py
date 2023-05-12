#!/usr/bin/python3

import sys

import src.expand_wordlist
import src.enumerate

TOOL_MAPPING = {
    "expand": src.expand_wordlist.expand_wordlist_argparse,
    "enumerate": src.enumerate.enumerate_wordlist_argparse
}

TOOL_ALIASES = {
    "enum": "enumerate",
    "exp": "expand"
}


# noinspection PyUnusedLocal
def generic_help_message(params: list[str] = None) -> None:
    help_msg = "Usage: python3 pwcrack-builder <tool> [args]"
    help_msg += f"\nPossible tools: {' '.join(TOOL_MAPPING)}"
    print(help_msg)


# noinspection PyArgumentList
def main():
    assert len(sys.argv) != 0, "What? How???"
    if len(sys.argv) == 1:
        generic_help_message()
        quit()

    tool = sys.argv[1]
    params = sys.argv[2:]

    for _ in TOOL_MAPPING.get(TOOL_ALIASES.get(tool, tool), generic_help_message)(params):
        print(_)


if __name__ == '__main__':
    main()
